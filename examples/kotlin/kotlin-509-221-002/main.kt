package com.example

import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import kotlinx.serialization.Serializable

@Serializable
data class Note(val id: Int, val text: String)

@Serializable
data class NoteCreate(val text: String)

fun main() {
    embeddedServer(Netty, port = 8080, module = Application::module).start(wait = true)
}

fun Application.module() {
    install(ContentNegotiation) { json() }

    val notes = mutableListOf<Note>()
    var nextId = 1

    routing {
        get("/health") {
            call.respond(mapOf("status" to "ok"))
        }
        get("/notes") {
            call.respond(notes)
        }
        post("/notes") {
            val body = call.receive<NoteCreate>()
            val note = Note(nextId++, body.text)
            notes += note
            call.respond(note)
        }
        delete("/notes/{id}") {
            val id = call.parameters["id"]?.toIntOrNull()
                ?: return@delete call.respondText("bad id", status = io.ktor.http.HttpStatusCode.BadRequest)
            if (notes.removeIf { it.id == id }) {
                call.respondText(status = io.ktor.http.HttpStatusCode.NoContent)
            } else {
                call.respondText("not found", status = io.ktor.http.HttpStatusCode.NotFound)
            }
        }
    }
}
