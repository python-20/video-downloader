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

## Pull Requests and Merging

feature branches will be merged into the default branch /trunk (master). 2 Approvals is required for any merging. Reviewers please pull and run the code and make sure it is working before approving.

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

