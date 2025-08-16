const envUrl = process.env.NEXT_PUBLIC_API_URL;

export const apiUrl =
  envUrl ??
  (process.env.NODE_ENV === "development"
    ? "http://127.0.0.1:8000" // fallback for local dev backend
    : "https://your-fake-news-detector-backend.herokuapp.com"); // prod fallback
