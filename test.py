import re

def repo_name(repo_url):
    #repo_url="https://github.com/lewisMachilika/screeenshot.git"
    #repo_url="https://lewis_machilika@bitbucket.org/nbsbank/self-onboarding-app.git"
    
    repo_name=re.findall("((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?",repo_url)

    repo_name=re.search("[^/]*$",repo_name[0][6])

    return repo_name.group(0)
print(repo_name('https://lewis_machilika@bitbucket.org/nbsbank/self-onboarding-app.git'))