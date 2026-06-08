(* LOGGING.mli *)
module type LOG = sig
  type t
  val log : t -> string -> unit
end

(* CONSOLE.ml *)
module Console : LOG = struct
  type t = unit
  let log () msg = print_endline msg
end

(* PREFIXED.ml *)
module Make (L : LOG) = struct
  let log_with_prefix prefix x msg =
    L.log x (prefix ^ ": " ^ msg)
end
