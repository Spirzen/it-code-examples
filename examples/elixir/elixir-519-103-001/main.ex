# mix.exs — {:plug_cowboy, "~> 2.7"}, {:jason, "~> 1.4"}
defmodule HelloPlug do
  use Plug.Router

  plug :match
  plug :dispatch

  get "/" do
    send_resp(conn, 200, Jason.encode!(%{ok: true}))
  end

  match _ do
    send_resp(conn, 404, "not found")
  end
end

# Plug.Cowboy.http(HelloPlug, [], port: 4000)
