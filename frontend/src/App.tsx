import { useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Lectures from "./pages/Lectures";
import LectureDetail from "./pages/LectureDetail";
import TestPage from "./pages/TestPage";
import Dashboard from "./pages/Dashboard";
import AdminPanel from "./pages/AdminPanel";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Compiler from "./pages/Compiler";
import VideoLectures from "./pages/VideoLectures";
import ProtectedRoute from "./routes/ProtectedRoute";
import useAuthStore from "./store/auth";
import { fetchProfile } from "./api/auth";

const App = () => {
  const { token, user, setUser } = useAuthStore();

  useEffect(() => {
    if (!token || user) return;
    fetchProfile()
      .then(setUser)
      .catch(() => undefined);
  }, [token, user, setUser]);

  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/lectures" element={<Lectures />} />
        <Route path="/lectures/:id" element={<LectureDetail />} />
        <Route path="/videos" element={<VideoLectures />} />
        <Route path="/compiler" element={<Compiler />} />
        <Route path="/tests/:id" element={<TestPage />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedRoute requireAdmin>
              <AdminPanel />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Layout>
  );
};

export default App;

