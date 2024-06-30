import mesop as me
import mesop.labs as mel
from crew import start_crew


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/CreateBlog",
  title="Linked In blog creator",
  
)
def app():
  mel.text_to_text(
    upper_case_stream,
    title="Create Blog",
  )


def upper_case_stream(text):
  blog_content = start_crew(text = text)
  return blog_content