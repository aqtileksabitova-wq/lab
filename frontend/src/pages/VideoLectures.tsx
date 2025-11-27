import { useEffect, useState } from "react";
import { fetchVideoLectures } from "../api/videos";
import type { VideoLecture } from "../types";

const VideoLectures = () => {
  const [videos, setVideos] = useState<VideoLecture[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchVideoLectures()
      .then(setVideos)
      .catch(() => setError("Не удалось загрузить видеолекции"))
      .finally(() => setLoading(false));
  }, []);

  if (loading)
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-indigo-200 border-t-indigo-600"></div>
          <p className="mt-4 text-slate-600">Загрузка видеолекций...</p>
        </div>
      </div>
    );
  if (error)
    return (
      <div className="rounded-xl border border-red-200 bg-red-50 p-6 text-center">
        <p className="text-red-600">{error}</p>
      </div>
    );

  return (
    <section className="space-y-8">
      <div className="rounded-2xl bg-gradient-to-r from-red-50 to-pink-50 p-8">
        <h1 className="text-4xl font-bold text-slate-900">Видеолекции</h1>
        <p className="mt-2 text-lg text-slate-600">
          Подборка актуальных докладов и курсов по C++ с YouTube
        </p>
        <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-white px-4 py-2 shadow-sm">
          <span className="text-sm font-semibold text-slate-700">Доступно видео:</span>
          <span className="rounded-full bg-red-100 px-3 py-1 text-sm font-bold text-red-600">
            {videos.length}
          </span>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {videos.map((video) => (
          <article
            key={video.id}
            className="group overflow-hidden rounded-2xl bg-white shadow-sm ring-1 ring-slate-200 transition-all hover:scale-[1.02] hover:shadow-xl"
          >
            <div className="relative aspect-video overflow-hidden bg-slate-900">
              <iframe
                className="h-full w-full transition-transform group-hover:scale-105"
                src={`https://www.youtube.com/embed/${video.youtube_id}`}
                title={video.title}
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>
            <div className="space-y-4 p-6">
              <div>
                <div className="mb-2 inline-flex items-center gap-2 rounded-full bg-red-50 px-3 py-1">
                  <span className="text-xs font-semibold uppercase text-red-600">{video.channel}</span>
                </div>
                <h3 className="text-lg font-bold text-slate-900 leading-tight">{video.title}</h3>
              </div>
              <p className="text-sm leading-relaxed text-slate-600">{video.short_description}</p>
              <div className="flex items-center justify-between border-t border-slate-100 pt-4">
                <div className="flex items-center gap-2 text-sm text-slate-500">
                  <span>⏱️</span>
                  <span className="font-medium">{video.duration_minutes} мин</span>
                </div>
                <a
                  className="flex items-center gap-1 rounded-lg bg-indigo-50 px-4 py-2 text-sm font-semibold text-indigo-600 transition-all hover:bg-indigo-100"
                  href={`https://youtu.be/${video.youtube_id}`}
                  target="_blank"
                  rel="noreferrer"
                >
                  YouTube
                  <span className="transition-transform group-hover:translate-x-1">→</span>
                </a>
              </div>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
};

export default VideoLectures;



