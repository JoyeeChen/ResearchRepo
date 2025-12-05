# prototyping_scripts
This folder contains scripts that are to be run in prototyping (i.e. exploratory code), as opposed to production (i.e. mature code).

Associated wandb project: https://wandb.ai/chen-joyee-team/ResearchRepoPrototyping

Some ideas for prototyping:

- Create a "representative random sample" function/method. What problem does this solve? Any successful eval run of more than 10 questions x 2 epochs is very likely to appear as a "great indistinguishable mass" of text. Suppose we want to qualitatively analyze such an eval run. We can't read through it all, so we would like to choose some way to select a smaller sample of it that still represents the eval as a whole. But the naivest/lowest-tech way to do that is relying on the viewer's own "random selection machine" inside their brain, which leads to systematic biases, and even if not, adds a layer of mental friction. So why not create a function/method that automatically randomly selects a particular amount/proportion of rows from the eval as a representative sample? 

For such a RRS, what should be the levels of input and output it should act upon? The broadest possible use seems to be acting on the level of the single .eval file for input, and outputting a single .eval file too. 

- Create unit tests for proposed questions that are to be added to AHB (or any other eval). What standards must that proposed question meet?

- Many other ideas that use https://inspect.aisi.org.uk/eval-sets.html