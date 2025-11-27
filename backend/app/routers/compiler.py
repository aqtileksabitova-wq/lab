"""Simple C++ compile-and-run endpoint using Piston API."""

from __future__ import annotations

import time
from typing import Literal

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/compiler", tags=["compiler"])

MAX_SOURCE_LENGTH = 50_000
PISTON_API_URL = "https://emkc.org/api/v2/piston/execute"

# Версии компиляторов в Piston API
PISTON_VERSIONS = {
    "c++17": "gcc-10.2.1",
    "c++20": "gcc-10.2.1",
}


class CompileRequest(BaseModel):
    source: str = Field(..., min_length=1, max_length=MAX_SOURCE_LENGTH)
    std: Literal["c++17", "c++20"] = Field(
        default="c++20",
        description="Стандарт C++ (поддерживаются только c++17 и c++20).",
    )


class CompileResponse(BaseModel):
    compile_stdout: str
    compile_stderr: str
    run_stdout: str
    run_stderr: str
    exit_code: int | None
    duration_ms: int


async def _compile_and_run(payload: CompileRequest) -> CompileResponse:
    """Компилирует и запускает код через Piston API."""
    start = time.perf_counter()
    
    # Определяем флаги компиляции в зависимости от стандарта
    std_flag = "c++20" if payload.std == "c++20" else "c++17"
    
    # Правильный формат для Piston API v2
    # Согласно документации: https://github.com/engineer-man/piston
    std_flag = "-std=c++20" if payload.std == "c++20" else "-std=c++17"
    
    piston_payload = {
        "language": "cpp",
        "version": "*",  # Используем последнюю доступную версию
        "files": [
            {
                "name": "main.cpp",
                "content": payload.source,
            }
        ],
        "stdin": "",
        "args": [],  # Аргументы для запуска программы
        "compile_timeout": 10000,
        "run_timeout": 5000,
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(PISTON_API_URL, json=piston_payload)
            
            # Получаем детальную информацию об ошибке
            if response.status_code != 200:
                error_detail = "Неизвестная ошибка"
                try:
                    error_data = response.json()
                    error_detail = error_data.get("message", str(error_data))
                except:
                    error_detail = response.text[:200] if response.text else f"HTTP {response.status_code}"
                
                duration_ms = int((time.perf_counter() - start) * 1000)
                return CompileResponse(
                    compile_stdout="",
                    compile_stderr=f"Ошибка API ({response.status_code}): {error_detail}",
                    run_stdout="",
                    run_stderr="",
                    exit_code=None,
                    duration_ms=duration_ms,
                )
            
            result = response.json()
    except httpx.TimeoutException:
        duration_ms = int((time.perf_counter() - start) * 1000)
        return CompileResponse(
            compile_stdout="",
            compile_stderr="Ошибка: превышено время ожидания ответа от сервера",
            run_stdout="",
            run_stderr="",
            exit_code=None,
            duration_ms=duration_ms,
        )
    except httpx.HTTPStatusError as e:
        duration_ms = int((time.perf_counter() - start) * 1000)
        error_detail = "Неизвестная ошибка"
        try:
            error_data = e.response.json()
            error_detail = error_data.get("message", str(error_data))
        except:
            error_detail = e.response.text[:200] if e.response.text else str(e)
        
        return CompileResponse(
            compile_stdout="",
            compile_stderr=f"Ошибка API ({e.response.status_code}): {error_detail}",
            run_stdout="",
            run_stderr="",
            exit_code=None,
            duration_ms=duration_ms,
        )
    except Exception as e:
        duration_ms = int((time.perf_counter() - start) * 1000)
        return CompileResponse(
            compile_stdout="",
            compile_stderr=f"Ошибка соединения: {str(e)}",
            run_stdout="",
            run_stderr="",
            exit_code=None,
            duration_ms=duration_ms,
        )

    duration_ms = int((time.perf_counter() - start) * 1000)

    # Обрабатываем ответ от Piston API
    compile_output = result.get("compile", {})
    run_output = result.get("run", {})

    compile_stdout = compile_output.get("stdout", "")
    compile_stderr = compile_output.get("stderr", "")
    run_stdout = run_output.get("stdout", "")
    run_stderr = run_output.get("stderr", "")
    exit_code = run_output.get("code", None)

    return CompileResponse(
        compile_stdout=compile_stdout,
        compile_stderr=compile_stderr,
        run_stdout=run_stdout,
        run_stderr=run_stderr,
        exit_code=exit_code,
        duration_ms=duration_ms,
    )


@router.post("/run", response_model=CompileResponse)
async def run_compiler(payload: CompileRequest):
    """Запускает компиляцию и выполнение кода через внешний API."""
    try:
        return await _compile_and_run(payload)
    except Exception as exc:
        return CompileResponse(
            compile_stdout="",
            compile_stderr=f"Неожиданная ошибка: {str(exc)}",
            run_stdout="",
            run_stderr="",
            exit_code=None,
            duration_ms=0,
        )