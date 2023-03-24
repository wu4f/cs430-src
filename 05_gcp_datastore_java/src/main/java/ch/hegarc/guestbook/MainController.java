package ch.hegarc.guestbook;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import ch.hegarc.guestbook.models.Guestbook;

@Controller
public class MainController {

	@GetMapping("/")
	public String greeting(Model model) {
		model.addAttribute("entries", new Guestbook().select());
		return "index";
	}

    @GetMapping("/sign")
    public String sign(Model model) {
        return "sign";
    }

    @RequestMapping(value = "/sign", method = RequestMethod.POST)
    public String signProcess() {
        // TODO
        return "redirect:/";
    }

}
