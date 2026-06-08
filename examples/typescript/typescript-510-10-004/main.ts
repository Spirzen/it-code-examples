type OkResponse = { status: "ok"; data: unknown };
type ValidationErrorResponse = {
  status: "validation_error";
  fields: string[];
};
type ServerErrorResponse = { status: "server_error"; code: number };

type ApiResponse =
  | OkResponse
  | ValidationErrorResponse
  | ServerErrorResponse;

type ErrorResponse = Exclude<ApiResponse, OkResponse>;
// ValidationErrorResponse | ServerErrorResponse

function logError(e: ErrorResponse): string[] | number {
  if (e.status === "validation_error") {
    return e.fields;
  }
  return e.code;
}
