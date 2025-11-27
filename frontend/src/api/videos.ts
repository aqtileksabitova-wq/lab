import api from "./client";
import type { VideoLecture } from "../types";

export const fetchVideoLectures = async () => {
  const { data } = await api.get<VideoLecture[]>("/video-lectures");
  return data;
};



