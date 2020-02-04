# Git branching

Trunk Based Development is used in this project. For a detail explanation please read: 
- [Trunk Based Development](https://trunkbaseddevelopment.com/)
- [Adopt a Git branching strategy](https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops)

## Naming conventions

```
type/description
```

types: features, bugfix, documentation, etc

### examples: 
- features/*which_feature*
- bugfix/*whatareyoufixing*

## Commenting your code

[Follow this issue on commenting your code](https://github.com/python-20/video-downloader/issues/16#issue-550940408)

It is very important for you to comment your code well to ensure others can understand your code and it's use. 
When possible, [add docstrings](https://www.pythonforbeginners.com/basics/python-docstrings/) to your functions and classes

## Pull Requests and Merging

Feature branches will be merged into the default branch /trunk (master). 2 Approvals is required for any merging. Reviewers please pull and run the code and make sure it is working before approving.

[Ensure that your commits & Pull Requests have meaningful messages and descriptions](https://chris.beams.io/posts/git-commit/), like:
```
Short description

Detailed description mentioning the additions and features you have made 

If any issues are solved via your commit/PR, add it in the description as well.
```

### Workflow
<ol>
<li>Pull from master to make sure you're working on an up to date version</li>
<li>Make the changes</li>
<li>Submit a pull request</li>
<li>Wait for Approval</li>
</ol>
If you're working on a bugfix or a new feature you can assign yourself to the related issue(s) so other people know you're working on it.

# Bugs
If you find a bug please submit a ticket in the issues section.

