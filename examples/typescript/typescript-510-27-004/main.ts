type ApiErrorBody = {
  error: {
    code: string;
    message: string;
    details?: Record<string, string[]>;
  };
};

function errorResponse(
  code: string,
  message: string,
  status: number,
): Response {
  const body: ApiErrorBody = { error: { code, message } };
  return new Response(JSON.stringify(body), { status });
}
