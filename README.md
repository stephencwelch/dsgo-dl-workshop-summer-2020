# Deep Learning Workshop

![](graphics/workshop_lander.gif)

## Agenda
1. Welcome!
2. Setting up your computing environment
3. Storytime - the summer project that took 50 years 
4. Getting image classification results fast with [fastai](https://docs.fast.ai/)
5. Bounding box detection
6. Semantic segmentation
7. Deploying models with [docker](https://github.com/moby/moby) and [flask](https://github.com/pallets/flask)
8. Reflection on studying and working in AI in 2020

## 1. Welcome!

### 1.1 Goal for Our Time Together
**Train and deploy deep learning computer vision models, and have some fun along the way :)**

## 2. Setting up your computing environment
Installing the software you need to train deep learning models can be difficult. For the purposes of this workshop, we're offering 3 recommended methods of setting up your computing environment. Your level of experience and access to machines, should help you determine which appraoch is right for you. 

| | Option | Pros | Cons | Cost | Instructions | 
| - | ------ | ---- | ---- | ---- | ------------ | 
| 1 | Google Colab | Virtually no setup required, start coding right away! | GPUs not always available, limited session times, limited RAM | Free! There's also a paid tier at [$10/month](https://colab.research.google.com/signup) | [Colab Setup](https://github.com/stephencwelch/dsgo-dl-workshop-summer-2020#1-setup-google-colab) |
| 2 | Virtual Machine | Highly configurable & flexible, pay for the performance level you need | Can be difficult to configure, only terminal-based interface | Starts ~$1/hour | [Azure VM Setup](https://github.com/stephencwelch/dsgo-dl-workshop-summer-2020#2-setup-an-azure-virtual-machine) |
| 3 | Your Own Linux GPU Machine | No recurring cost, complete control over hardware. | High up-front cost, takes time to configure. | $1000+ fixed up front cost | [Linux Setup](https://github.com/stephencwelch/dsgo-dl-workshop-summer-2020#3-setup-on-your-own-gpu-machine-running-linux) |


### 2.1 Setup Google Colab


### 2.2 Setup an Azure Virtual Machine


### 2.3 Setup on Your Own GPU Machine Running Linux


## 3. Storytime - the summer project that took 50 years

### 3.1 The Original Problem 
![](graphics/original_mit_crew-01.png)

**Computer Vision** has a very interesting history. It's roots really go all the way back to the beginning of computing and **Artifical Intelligence.** In these early days, it was unknown just how easy or difficult it would be to recreate the function of the human visual system. A great example of this is the 1966 MIT Summer Vision Project. Marvin Minsky and Seymour Papert, co-directors of the MIT AI Labratory, begun the summer with some ambitious goals:

![](graphics/summer_project_abstract-01.png)

Minsky and Papert assigned Gerald Sussman, an MIT undergraduate studunt as project lead, and setup specific goals for the group around recognizing specific objects in images, and seperating these objects from their backgrounds. 

![](graphics/summer_project_goals-01.png)

Just how hard is it to acheive the goals Minsky and Papert laid out? How has the field of computer vision advance since that summer? Are these tasks trivial now, 50+ years later? Do we understand how the human visual system works? Just how hard *is* computer vision and how far have we come?

### 3.2 Computer Vision is Hard

Interestingly, comptuer vision  turns out to be significantly harder than people first expected. Part of the challenge here is that vision, like other processes that involve the brain, can be a bit hard to pin down. 

What exactly does it mean to see? To have vision?

You’re probably using your own vision system right now to read these words, but if I asked you to break down piece by piece how exactly your brain is processing the light that hits your retina into meaningful information, you would have a really tough time. 

The vision researchers Peter Hart and Richard Duda had a really nice way of putting this when they wrote one of the first [computer vision books](https://www.amazon.com/Pattern-Classification-Scene-Analysis-Richard/dp/0471223611): 

> "Paradoxically, we are all expert at perception, but none of us knows much about it."

Now, as you may know, it’s taken longer than we thought, but we have made some good progress in computer vision. Today, the computer vision systems we’ve built are even better than humans at certain tasks. 

### 3.3 Everything Popular is Wrong

In fact, in today's workshop, **we'll achieve exactly what Minsky and Papert set out to do.** And what I think makes this *really* interesting, is that just 10 years ago, this really would not have been possible. You see, it really took around 50 years to achieve the goals of the MIT summer project. 

Now, just becuase it took 50 years to acheive these goals, this does not mean that we should only pay attention to recent breakthroughs. Computer vision has a rich and detailed history that deeply informs that work we see today. One aspect that we would be remiss if we didn't breifly discuss is the tradeoff between **analytical and empirical techniques**.

### Part of an analytical pipeline for recognizing a brick

![](graphics/hough_pipeline_short.gif)

Throughout the history of computer vision (and computation and philosophy), we've seen a natural oscillation and competition between techniques that are grounded in reason (analytical), and techniques that are grounding in observation or data. Today we live in a time that is very much dominated by empricism. Decisions must be data driven. In machine learning and computer vision, we see huge breakthroughs from emprical techniques that learn from data, such as deep learning. 

So as we dive into building and training our own deep learning models, just remember that this is only one approach. We've seen huge performance increases from empirical approaches recently, and that's what we'll be spending our time on here. 

### 3.4 Our dataset for the day
To solve the original computer vision problem using an emprical appraoch, we're going to need some data. We'll be using a fun little dataset called bbc1k. This dataset was collected in the spirit of the original MIT summer project, and contains 1000 images of bricks, balls, and cylinders against cluttered backgrounds. 

![](../graphics/bbc1k.gif)

You can download the dataset [here](http://www.welchlabs.io/unccv/deep_learning/bbc_train.zip), or with the download script in the util directory of this repo:

```
python util/get_and_unpack.py -url http://www.welchlabs.io/unccv/deep_learning/bbc_train.zip
```

![](../graphics/bbc_sample.jpg)


 BBC-1k dataset includes ~1000 images ncluding classification, bounding box, and segmentation labels mportantly, each image only contains one brick, ball or cylinder.




### 3.5 Further Reading & Viewing
- [Computer Vision Course at UNCC](https://github.com/unccv/uncc_course_overview)
- [Learning to See](https://www.youtube.com/watch?v=i8D90DkCLhI)
- [Great Book on the History of AI](https://www.amazon.com/Ai-Tumultuous-History-Artificial-Intelligence/dp/0465029973)

## 4. Getting image classification results fast with fastai


## 6. Deploying models with docker and flask


## 7. Reflection on studying and working in AI in 2020
