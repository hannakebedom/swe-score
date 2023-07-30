from github import Github

g = Github("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")

print(g.get_user().name)

# for repo in g.get_user().get_repos():
#     print(repo.name)
#     repo.edit(has_wiki=False)
#     # to see all the available attributes and methods
#     print(dir(repo))