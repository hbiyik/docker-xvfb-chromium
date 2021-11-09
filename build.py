import os

uname = "boogiepy"
platforms = {"armhf": "sha256:2ed3381dc520b76100dd6231c4d6cdbd76acec0d60a1532b9ec816f28ec17517",
             "arm64": "sha256:00bdd2cd7e6bba43444604b453d7895d5bd5fc52ec2a7b0afd2c390a9900b58b",
             "amd64": "sha256:edb0a5915350ee6e2fedd8f9d0fe2e7f956f7a58f7f41b5e836e0bb7543e48a1",
             "i386": "sha256:a10944bbb2cc079633dcbd85be26a633814cce8fe453e8130017d8f749873c70"}

for tc, sha in platforms.items():
    cmd = "docker build -t %s/chromium-xvfb-%s --build-arg HASH=%s ." % (uname, tc, sha)
    print(cmd)
    os.system(cmd)

