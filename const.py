MAGIC_WORD: str = "we got it boys!"
TERM_MSG = lambda x: x.get("content", "").find(MAGIC_WORD) >= 0
REPLAYS: int = 2
INTERNAL_CONV_REPLAYS: int = 1
SUMMARY_PROMPT = """
Return review into as JSON object only:
{'Reviewer': '', 'Review': ''}
"""
INTERNAL_CONV_SUMMARY = """
Aggregate feedback from all reviewers and give final suggestions on the roadmap.
"""
