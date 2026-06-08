import type { Request, Response } from "express";
import type { CreateUserDto } from "./types/dto.js";

type ApiOk<T> = { ok: true; data: T };
type ApiErr = { ok: false; error: string };
type ApiResponse<T> = ApiOk<T> | ApiErr;

function isCreateUserDto(body: unknown): body is CreateUserDto {
  if (typeof body !== "object" || body === null) return false;
  const o = body as Record<string, unknown>;
  return typeof o.email === "string" && typeof o.name === "string";
}

export async function postUser(
  req: Request,
  res: Response<ApiResponse<User>>,
): Promise<void> {
  if (!isCreateUserDto(req.body)) {
    res.status(400).json({ ok: false, error: "Invalid body" });
    return;
  }
  const result = createUser(req.body, new Set());
  if (!result.ok) {
    const status = result.error === "conflict" ? 409 : 400;
    res.status(status).json({ ok: false, error: result.error });
    return;
  }
  res.status(201).json({ ok: true, data: result.value });
}
