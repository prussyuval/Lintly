"""
Formats text that will be posted to Pull Requests.
"""
import os

from jinja2 import Environment, FileSystemLoader

from .constants import LINTLY_IDENTIFIER


TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')


env = Environment(
    loader=FileSystemLoader(TEMPLATES_PATH),
    autoescape=False
)


def build_pr_comment(config, violations):
    """
    Creates a Markdown representation of the comment to be posted to a pull request.
    :return: The comment
    """
    template = env.get_template('pr_comment.txt')
    return template.render(violations=violations, LINTLY_IDENTIFIER=LINTLY_IDENTIFIER)


def build_pr_review_line_comment(violation):
    """
    Creates a Markdown representation of the comment to be posted to a pull request.
    :return: The comment
    """
    template = env.get_template('pr_review_line_comment.txt')
    return template.render(violation=violation, LINTLY_IDENTIFIER=LINTLY_IDENTIFIER)


def build_check_line_comment(violation):
    template = env.get_template('check_line_comment.txt')
    return template.render(violation=violation)


def build_pr_review_body(all_violations, diff_violations):
    template = env.get_template('pr_review_body.txt')
    return template.render(
        all_violations=all_violations, diff_violations=diff_violations, LINTLY_IDENTIFIER=LINTLY_IDENTIFIER
    )
