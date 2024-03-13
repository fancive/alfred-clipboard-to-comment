import subprocess
from workflow import Workflow, ICON_NOTE
import sys


# Get clipboard data
def get_clipboard_data():
    p = subprocess.Popen(["pbpaste"], stdout=subprocess.PIPE)
    return p.communicate()[0].decode("utf-8")


# Convert to function comment
def convert_to_comment(content):
    comments = []
    for line in content.split("\n"):
        if line == "":
            comments.append("//")
        else:
            # Split long lines
            while len(line) > 80:
                part, line = line[:80], line[80:]
                comments.append("// " + part)
            comments.append("// " + line)
    return "\n".join(comments)


# Process clipboard and add comment to workflow
def process_input(workflow, input_str):
    comment = convert_to_comment(input_str)
    workflow.add_item(
        title="Converted to Comment",
        subtitle="Clipboard content converted to function comment",
        arg=comment,
        valid=True,
        icon=ICON_NOTE,
    )


def main(workflow):
    # Use clipboard content if no argument is provided
    input_str = get_clipboard_data().strip()
    process_input(workflow, input_str)
    workflow.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
