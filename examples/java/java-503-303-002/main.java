
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/notes")
public class NoteController {

    private final NoteService service;

    public NoteController(NoteService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<NoteService.Note> create(@Valid @RequestBody CreateNoteRequest req) {
        NoteService.Note saved = service.create(req.text());
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }

    @GetMapping("/{id}")
    public NoteService.Note get(@PathVariable long id) {
        return service.find(id).orElseThrow(() -> new NoteNotFoundException(id));
    }
}
