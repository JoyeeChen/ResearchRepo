# High level design decisions

Note: "Tips and Code" shall refer to https://www.alignmentforum.org/posts/6P8GYb4AjtPXx6LLB/tips-and-code-for-empirical-research-workflows and "Apollo" shall refer to Apollo Research's Engineering Guide at https://docs.google.com/document/d/1LJedFJKrGs7vi-xA1ucQQxj_y85Z9x4lEmf4sFgeX6g/edit?tab=t.0

Q: Why not use google colab notebooks and their GPUs for inference? 

A: (Epistemic status: somewhat firm) Will elaborate later.

Q: Why use Together.ai for inference? (I'm not talking about training/tuning here)

A: (Epistemic status: firm but not totally firm.) It's directly recommended in Tips and Code. Also, around Dec 2, I tried colab and runpod (nearest competitors; runpod recommended in both Tips and Code and Apollo) but each had basic integration issues then. (Like runpod needing the logistical overhead of a remote machine, I think?) Plus, together.ai works just as well in a colab notebook vs non-colab jupyter notebook (vscode or otherwise) vs a python file. This has many advantages, one of which is to ease portability between prototyping and production code, which might require going from notebook to non-notebook environments.

Q: Why integrate inspect (for evals) with WandB, instead of just using inspect?

A: I consider WandB to be a modern, mature, and stable technology for the important needs of logging things for future use as frictionlessly as possible, as well as seeing all of one's work at a glance with low friction. It's also directly recommended in Tips and Code as well as Apollo. The natural way I do that is via the bridging package https://inspect-wandb.readthedocs.io/en/latest/index.html.

Q: Why use uv for package management, instead of just pip or other competitors?

A: Directly recommended in Tips and Code. Also a great deal of AI safety research packages' documentation (like that of Inspect Evals and Inspect-Wandb) use uv in their tutorials.

Q: Why use separate folders for scripts vs non-scripts? And why use separate folders for prototyping code vs production code?

A: Broadly justified by Tips and Code as well as Apollo, and talking to some research engineers in person. Both guides have a general spirit of "two modes of research engineering" I'd like to capture.
