package cn.inspiry.jenkinswebdemo;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class helloController {
    @RequestMapping("/")
    public String hello() {
        return "<h1> <font color=#ff0000> Hello CICD home works</font>";
    }
}
