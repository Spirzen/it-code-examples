@Controller
public class CommentController {
    
    @GetMapping("/comments")
    public String showComments(Model model) {
        List<Comment> comments = commentRepository.findAll();
        
        // Экранирование текста комментариев
        List<Comment> safeComments = comments.stream()
            .map(comment -> new Comment(
                comment.getId(),
                escapeHtml(comment.getAuthor()),
                escapeHtml(comment.getText())
            ))
            .collect(Collectors.toList());
        
        model.addAttribute("comments", safeComments);
        return "comments";
    }
    
    private String escapeHtml(String input) {
        if (input == null) return null;
        return input.replace("&", "&amp;")
                   .replace("<", "&lt;")
                   .replace(">", "&gt;")
                   .replace("\"", "&quot;")
                   .replace("'", "&#x27;");
    }
}
