package ch.hegarc.guestbook;

import ch.hegarc.guestbook.models.Entry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class MainController {

    @Autowired
    private GuestbookService guestbookService;

	@GetMapping("/")
	public String greeting(Model model) {
		model.addAttribute("entries", guestbookService.select());
		return "index";
	}

    @GetMapping("/sign")
    public String sign(Model model) {
        model.addAttribute("entry", new Entry());
        return "sign";
    }

    @PostMapping( "/sign")
    public String signProcess(@ModelAttribute Entry entry) {
        guestbookService.insert(entry);
        return "redirect:/";
    }

}
