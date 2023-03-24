package ch.hegarc.guestbook;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ModelAttribute;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Mustache.Compiler;
import com.samskivert.mustache.Template.Fragment;


import java.io.IOException;
import java.io.Writer;
import java.util.Map;

@ControllerAdvice
class LayoutAdvice {
	private final Mustache.Compiler compiler;

	@Autowired
	public LayoutAdvice(Compiler compiler) {
		this.compiler = compiler;
	}

	@ModelAttribute("layout")
	public Mustache.Lambda layout(Map<String, Object> model) {
		return new Layout(compiler);
	}
}
class Layout implements Mustache.Lambda {

  String body;

  private Compiler compiler;

  public Layout(Compiler compiler) {
    this.compiler = compiler;
  }

  @Override
  public void execute(Fragment frag, Writer out) throws IOException {
    body = frag.execute();
    compiler.compile("{{>layout}}").execute(frag.context(), out);
  }
}
