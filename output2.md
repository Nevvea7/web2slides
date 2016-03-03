CSCI-UA.202 Operating Systems  
2015-16 Spring  
Allan Gottlieb  
Tuesday Thursday 3:30-4:45  
Room 109 CIWW

Start Lecture #1

# Chapter -1 Administrivia

I start with chapter -1 so that when we get to chapter 1, the numbering will
agree with the text.

## (-1).1 Contact Information

  * email: my-last-name AT nyu DOT edu (best method)
  * web: [cs.nyu.edu/~gottlieb](cs.nyu.edu/~gottlieb)
  * brick and mortar: 715 Broadway, Room 712
  * phone: 212 998 3344

## (-1).2 Course Web Page

There is a web site for the course. You can find it from my home page, which
is http://cs.nyu.edu/~gottlieb

  * You can find these lecture notes on the course home page. Please let me know if you can't find them.
  * The notes are updated as bugs are found or improvements made. As a result, I do not recommend printing the notes now (if at all).
  * I will place markers at the end of each lecture after the lecture is given. For example, the Start Lecture #1 marker above can be thought of as End Lecture #0.

## (-1).3 Textbook

The course text is Tanenbaum, "Modern Operating Systems", Forth Edition (4e).  
We will cover nearly all of the first six chapters, plus some material from
later chapters.

I once used a book by Finkel, which is now out of print, but is [ available on
the web. ](ftp://ftp.cs.uky.edu/cs/manuscripts/vade.mecum.2.pdf)

## (-1).4 Email, and the Mailman Mailing List

  * You should have all been automatically added to the mailing list for this course and should have received a test message from me dated 15 January 2016.
  * If that automatic system didn't work, you can sign up for the mailing list by clicking [ here. ](http://www.cs.nyu.edu/mailman/listinfo/CSCI_UA_0202_001_sp16) If both methods fail, send me an email and I will have the systems group add you. This may well happen to students who join the class late. 
  * Membership on the list is **Required**; I assume that messages I send to the mailing list are read.
  * If you want to send mail just to me, use my-last-name AT nyu DOT edu not the mailing list.
  * Questions on the labs should go to the mailing list. You may answer questions posed on the list as well. Note that replies **are sent to the list**.
  * I will respond to all questions. If another student has answered the question before I get to it, I will confirm if the answer given is correct.
  * Please use proper mailing list etiquette. 
    * Send **plain text** messages rather than (or at least in addition to) html.
    * Use Reply to contribute to the current thread, but **NOT** to start another topic.
    * If quoting a previous message, trim off irrelevant parts.
    * Use a descriptive Subject: field when starting a new topic.
    * Do not use one message to ask two unrelated questions.
    * Do **NOT** make the mistake of sending your completed lab assignment to the mailing list. This is not a joke; several students have made this mistake in past semesters.
  * I prefer that when you respond to a message, you either place your reply after the original text or interspersed with it (rather than putting your reply at the top).  
This preference is most relevant for detailed questions that lead to serious
conversations involving many messages. I find it quite useful when reviewing a
serious conversations to have the entire conversation in chronological order.  
I believe you would also find it useful when reviewing for an exam.

## (-1).5 Grades

Grades are based on the labs and exams; the weighting will be approximately  
25%*LabAverage + 30%*MidtermExam + 45%*FinalExam (but see homeworks below).

## (-1).6 The Upper Left Board

I use the upper left board for lab/homework assignments and announcements. I
should never erase that board. Viewed as a file it is group readable (the
group is those in the room), appendable by just me, and (re-)writable by no
one. If you see me start to erase an announcement, let me know.

I try very hard to remember to write all announcements on the upper left board
and I am normally successful. If, during class, you see that I have forgotten
to record something, please let me know. **HOWEVER**, if I forgot and no one
reminds me, the assignment has still been given.

## (-1).7 Homeworks and Labs

I make a distinction between homeworks and labs.

Labs are

  * _Required_.
  * Due several lectures later (date given on assignment).
  * Given in the notes and on NYU Classes with supplemental material on separate web pages. Your solution is submitted via NYU Classes.
  * Graded and form part of your final grade.
  * Penalized for lateness. The penalty is 1 point per day up to 30 days; then 3 points per day.
  * This penalty is **much** too mild; but it is enforced.
  * Near the final exam a **firm** deadline will be set after which no labs will be accepted.
  * Computer programs you must write.

Homeworks are

  * Optional.
  * Due the beginning of the _Next_ lecture.
  * Not accepted late.
  * Mostly from the book.
  * The assignment is given in the notes and Classes; your solution is submitted via NYU Classes.
  * Checked for completeness and graded 0/1/2.
  * Able to help, but not hurt, your final grade.

### (-1).7.1 Homework Numbering

Homeworks are numbered by the class in which they are assigned. So any
homework given today is homework #1. Even if I do not give homework today, the
homework assigned next class will be homework #2. Unless I explicitly state
otherwise, all homeworks assignments can be found in the class notes. So the
homework present in the notes for lecture #n is homework #n (even if I
inadvertently forgot to write it to the upper left board).

### (-1).7.2 Doing Labs on non-NYU Systems

You may _develop_ (i.e., write and test) lab assignments on any system you
wish, e.g., your laptop. However, ...

  * You are responsible for any non-nyu machine. I extend deadlines if the nyu machines are down, not if yours are. So you should back up any work done on your own machine.
  * You should test your assignments on the nyu systems, for this class that means mauler.cims.nyu.edu. More on how to do this later.
  * In an ideal world, a program written in a high level language such as Python, Java, C, or C++ that works on one system would also work on any other system. Sadly, this ideal is not always achieved, despite marketing claims to the contrary. So, although you may _develop_ your lab on any system, you must ensure that it _runs_ on mauler, which the TAs will use when grading your labs.
  * You submit your labs using NYU Classes.

### (-1).7.2.1 Testing Your Labs on mauler.cims.nyu.edu

I feel it is important for CS majors to be familiar with basic client-server
computing (related to cloud computing) in which one develops on a client
machine (for us, most likely one's personal laptop), but runs on a remote
server (for us, mauler.cims.nyu.edu). This requires three steps.

  1. Obtaining an account on mauler (and access.cims.nyu.edu).
  2. Copying files (the lab) from your system to mauler.
  3. Logging into mauler and running the lab.

I have supposedly given you each an account on mauler (and access), which
takes care of step 1. Accessing mauler and access is different for different
client (laptop) operating systems.

  * If you have a unix based system (e.g., linux) you are ready to try it. From a terminal, type ssh username@access.cims.nyu.edu, where username is your username on home.nyu.edu (i.e., your netid). It should print an obnoxious warning and ask for your password. Again use the one from home.nyu.edu. You should now be logged into a unix machine so try ls. You use scp (secure copy) to copy files from one unix machine to another.
  * If you have MacOS, you use the same commands as for unix (the core of MacOS is unix). However, some versions of the MacOS terminal emulator default to rich text (instead of plain, ascii text). Once you convert to (or are lucky enough to have) a plain text terminal, you proceed just as for a unix machine.
  * If you have MS Windows, you need to get two programs: PuTTY and WinSCP. Both are readily available for no cost (I think nyu/its has one of them). Please get them right away and I will demo putty/winscp next class.

### (-1).7.3 Obtaining Help with the Labs

Good methods for obtaining help include

  1. Asking me during office hours (see web page for my hours).
  2. Asking the mailing list.
  3. Asking another student.
  4. But ...  
Your lab must be your own.  
That is, each student must submit a unique lab. Naturally, simply changing
comments, variable names, etc. does **not** produce a unique lab.

### (-1).7.4 Computer Language Used for Labs

You may write your lab in Java, C, or C++.

## (-1).8 A Grade of Incomplete

The rules for incompletes and grade changes are set by the school and not the
department or individual faculty member.

The rules set by CAS can be found in [
here](http://bulletin.cas.nyu.edu/page/academic.policies#EXAMINATIONS). They
state:

> The grade of I (Incomplete) is a temporary grade that indicates that the
student has, for good reason, not completed all of the course work but that
there is the possibility that the student will eventually pass the course when
all of the requirements have been completed. A student must ask the instructor
for a grade of I, present documented evidence of illness or the equivalent,
and clarify the remaining course requirements with the instructor.

>

> The incomplete grade is not awarded automatically. It is not used when there
is no possibility that the student will eventually pass the course. If the
course work is not completed after the statutory time for making up
incompletes has elapsed, the temporary grade of I shall become an F and will
be computed in the student's grade point average.

>

> All work missed in the fall term must be made up by the end of the following
spring term. All work missed in the spring term or in a summer session must be
made up by the end of the following fall term. Students who are out of
attendance in the semester following the one in which the course was taken
have one year to complete the work. Students should contact the College
Advising Center for an Extension of Incomplete Form, which must be approved by
the instructor. Extensions of these time limits are rarely granted.

>

> Once a final (i.e., non-incomplete) grade has been submitted by the
instructor and recorded on the transcript, the final grade cannot be changed
by turning in additional course work.

## (-1).9 Academic Integrity Policy

This email from the assistant director, describes the departmental policy.

    
    
      Dear faculty,
    
      The vast majority of our students comply with the
      department's academic integrity policies; see
    
      www.cs.nyu.edu/web/Academic/Undergrad/academic_integrity.html
      www.cs.nyu.edu/web/Academic/Graduate/academic_integrity.html
    
      Unfortunately, every semester we discover incidents in
      which students copy programming assignments from those of
      other students, making minor modifications so that the
      submitted programs are extremely similar but not identical.
    
      To help in identifying inappropriate similarities, we
      suggest that you and your TAs consider using Moss, a
      system that automatically determines similarities between
      programs in several languages, including C, C++, and Java.
      For more information about Moss, see:
    
      http://theory.stanford.edu/~aiken/moss/
    
      Feel free to tell your students in advance that you will be
      using this software or any other system.  And please emphasize,
      preferably in class, the importance of academic integrity.
    
      Rosemary Amico
      Assistant Director, Computer Science
      Courant Institute of Mathematical Sciences
    

The university-wide policy is described [ here ](//www.nyu.edu/about/policies-
guidelines-compliance/policies-and-guidelines/academic-integrity-for-students-
at-nyu.html)

# Chapter 0 Interlude on Linkers

Originally called a _linkage editor_ by IBM.

A linker is an example of a _utility_ program included with an operating
system distribution. Like a compiler, the linker is not part of the operating
system per se, i.e., it does not run in supervisor mode. Unlike a compiler it
is OS dependent (what object/load file format is used) and is not (normally)
language dependent.

## 0.1 What does a Linker Do?

Link, of course.

When the compiler and assembler have finished processing a module, they
produce an **object module** that is almost runnable. There are two remaining
tasks to be accomplished before object modules can be run. Both are involved
with linking (that word, again) together multiple object modules. The tasks
are **relocating relative addresses** and **resolving external references**;
each is described just below.

The output of a linker is called a **load module** because, with relative
addresses relocated and the external addresses resolved, the module is ready
to be loaded and run.

![relocate](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/relocate.png)

### 0.1.1 Relocating Relative Addresses

The compiler and assembler (mistakenly) treat each module as if it will be
loaded at location zero. For example, the machine instruction  
    jump 120  
is used to indicate a jump to location 120 of the current module.

To convert this **relative address** to an **absolute address**, the linker
adds the **base address** of the module to the relative address. The base
address is the address at which this module will be loaded.

For example, assume a module is to be loaded starting at location 2300 and
contains the above instruction  
    jump 120  
The linker changes this instruction to  
    jump 2420

How does the linker know that the module is to be loaded starting at location
2300?

  * It processes the modules one at a time. The first module is to be loaded at location zero. So relocating the first module is trivial (adding zero). We say that the relocation constant is zero.
  * After processing the first module, the linker knows its length (say that length is L1).
  * Hence the next module is to be loaded starting at L1, i.e., the relocation constant is L1.
  * In general the linker keeps the sum of the lengths of all the modules it has already processed; this sum is the relocation constant for the next module.
![resolve](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/resolve.png)

### 0.1.2 Resolving External References

If a C (or Java, or Pascal, or Ada, etc) program contains a function call
`f(x)`  to a function `f()` that is compiled separately, the resulting object
module must contain some kind of jump to the beginning of f.

  * But this is impossible!
  * When the program is compiled, the compiler and assembler do _not_ know the location of f() so there is _no way_ they can supply the starting address.
  * Instead a dummy address is supplied and a notation made that this address needs to be filled in with the location of f(). This is called a **use** of f().
  * The object module containing the **definition** of f() contains a notation that f() is being defined and gives the relative address of the definition, which the linker converts to an absolute address (as above).
  * The linker then changes all uses of f() to the correct absolute address.

### 0.1.3 An Example from Lab 1

To see how a linker works lets consider the following example, which is the
first dataset from lab #1. The description in lab1 is more detailed.

The target machine is word addressable and each word consists of 4 decimal
digits. The first (leftmost) digit is the opcode and the remaining three
digits form an address.

Each object module contains three parts, a definition list, a use list, and
the program text itself. Each definition is a pair (sym, loc) signifying that
this symbol is defined at this location.

Each use is again a pair (sym, loc), but this time signifying that sym is used
in the linked list started at loc. The address in loc points to the next use
of sym. An address of 777 is the sentinel ending the list

The program text consists of a count N followed by N pairs (type, word), where
word is a 4-digit instruction as described above and type is a single
character indicating if the address in the word is Immediate, Absolute,
Relative, or External.

The actions taken by the linker depend on the type of the address, as we now
illustrate. Consider the first input set from the lab.

    
    
      Input set #1
      4
      1 xy 2
      1 z 4
      5 R 1004  I 5678  E 2777  R 8002  E 7002
      0
      1 z 3
      6 R 8001  E 1777  E 1001  E 3002  R 1002  A 1010
      0
      1 z 1
      2 R 5001  E 4777
      1 z 2
      1 xy 2
      3 A 8000  E 1777  E 2001
    

The first pass simply finds the base address of each module and produces the
symbol table giving the values for xy and z (2 and 15 respectively). The
second pass does the real work using the symbol table and base addresses
produced in pass one.

The resulting output (shown below) is more detailed than I expect you to
produce. The detail is there to help me explain what the linker is doing. All
I would expect from you is the symbol table and the rightmost column of the
memory map.

Output for Linked List format with addr-type a letter

    
    
      Symbol Table
          xy=2
          z=15
      Memory Map
      +0
      0:       R 1004      1004+0 = 1004
      1:       I 5678               5678
      2: xy:   E 2777 ->z           2015
      3:       R 8002      8002+0 = 8002
      4:       E 7002 ->z           7015
      +5
      0        R 8001      8001+5 = 8006
      1        E 1777 ->z           1015
      2        E 1001 ->z           1015
      3        E 3002 ->z           3015
      4        R 1002      1002+5 = 1007
      5        A 1010               1010
      +11
      0        R 5001      5001+11= 5012
      1        E 4777 ->z           4015
      +13
      0        A 8000               8000
      1        E 1777 ->xy          1002
      2 z:     E 2001 ->xy          2002
    

**Note**: It is faster (less I/O) to do a one pass approach, but is harder since you need fix-up code whenever a use occurs in a module that precedes the module with the definition.

Historical note: The linker on unix was mistakenly called ld (for loader),
which is unfortunate since it links but does not load.

Unix was originally developed at Bell Labs; the seventh edition of unix was
made publicly available (perhaps earlier ones were somewhat available). The
7th ed man page for ld begins (see http://cm.bell-labs.com/7thEdMan).

    
    
        .TH LD 1
        .SH NAME
        ld \- loader
        .SH SYNOPSIS
        .B ld
        [ option ] file ...
        .SH DESCRIPTION
        .I Ld
        combines several
        object programs into one, resolves external
        references, and searches libraries.
      

By the mid 80s the Berkeley version (4.3BSD) man page referred to ld as link
editor and this more accurate name is now standard in unix/linux
distributions.

During the 2004-05 fall semester a student wrote to me:

> BTW - I have meant to tell you that I know the lady who wrote ld. She told
me that they called it loader, because they just really didn't have a good
idea of what it was going to be at the time.

[ The wikipedia reference ](http://en.wikipedia.org/wiki/Linker)

**Lab #1:** Implement a two-pass linker. See the class home page and NYU Classes for details.

Start Lecture #2

# Chapter 1 Introduction

**Homework:** Read Chapter 1 (Introduction)

#### Levels of abstraction (virtual machines)

Software is often implemented in layers (so is hardware, but that is not the
subject of this course). The higher layers use the facilities provided by
lower layers.

Alternatively said, the upper layers are written using a more powerful and
more abstract virtual machine than the lower layers.

In yet other words, each layer is written as though it runs on the virtual
machine supplied by the lower layers and in turn provides a more abstract
(pleasant) virtual machine for the higher layers to run on.

Using a broad brush, the layers are.

  1. Applications (e.g., web browser) and utilities (e.g., compiler, linker).
  2. User interface (UI). It may be text oriented (Unix/Linux shell, DOS prompt) or graphical (GUI, e.g., MS Windows, Gnome/KDE, MAC).
  3. Libraries (e.g., libc).
  4. The OS proper (the kernel).
  5. Hardware.

An important distinction is that the kernel runs in
**privileged/kernel/supervisor** mode; whereas your programs, as well as
compilers, editors, shell, linkers, browsers, etc. run in **user** mode. This
means that the OS can access all the hardware and execute all possible
instructions.

In contrast user programs cannot directly modify the hardware; for example I/O
instructions are normally privileged. So the programs you and I write
**cannot** perform I/O; but they can ask the OS to perform the I/O for them.

The kernel is itself normally layered, e.g.

  1. (Machine independent) files and filesystems.
  2. (Machine independent) I/O.
  3. (Machine dependent) device drivers.

The machine independent I/O layer is written assuming virtual (i.e. idealized)
hardware. For example, the machine independent I/O portion can access a
certain byte in a given file. In reality, I/O devices, e.g., disks, have no
support or knowledge of files; these devices support only blocks. Lower levels
of the software implement files in terms of blocks.

Often the machine independent part is itself more than one layer.

The term Operating System is not well defined. Is it just the kernel, i.e.,
the portion run in supervisor mode? How about the libraries? The utilities?
All these are certainly **system software** but it is not clear how much is
part of the OS.

## 1.1 What is an operating system?

As mentioned above, the OS raises the abstraction level by providing a higher
level virtual machine. A second related key objective for the OS is to manage
the resources provided by this virtual machine.

### 1.1.1 The Operating System as an Extended Machine

The kernel itself raises the level of abstraction and hides details. For
example a user (of the kernel) can write() to a file (a concept not present in
hardware) and without knowing whether the file resides on a solid-state-disk
(SSD), an internal scsi disk, or a local USB disk. The user can also ignore
issues such as whether the file is stored contiguously or is broken into
blocks.

Well designed abstractions are a key to managing complexity.

### 1.1.2 The Operating System as a Resource Manager

The kernel must manage the resources to resolve conflicts between users. Note
that when we say users, we are not referring directly to humans, but instead
to processes (typically) running on behalf of humans.

Often the resource is shared or _multiplexed_ between the users. This can take
the form of _time-multiplexing_, where the users take turns (e.g., the
processor resource) or _space-multiplexing_, where each user gets a part of
the resource (e.g., a disk drive).

With sharing comes various issues such as protection, privacy, fairness, etc.

#### How is an OS Fundamentally Different from (say) a Compiler?

Answer: Concurrency! Per Brinch Hansen in _Operating Systems Principles_
(Prentice Hall, 1973) writes.

> The main difficulty of multiprogramming is that concurrent activities can
interact in a time-dependent manner, which makes it practically impossibly to
locate programming errors by systematic testing. Perhaps, more than anything
else, this explains the difficulty of making operating systems reliable.

**Homework:** 1\. (Unless otherwise stated, problems numbers are from the end of the current chapter in Tanenbaum.) What are the two main functions of an operating system?

## 1.2 History of Operating Systems

The subsection headings describe the hardware as well as the OS; we are
naturally more interested in the latter. These two development paths are
related as the improving hardware enabled the more advanced OS features.

### 1.2.1 The first Generation (1945-55): Vacuum Tubes (and No OS)

One user (program; perhaps several humans) at a time. Any operating-system-
like functionality that was needed was part of the user's program.

Although this time frame predates my own usage, computers without serious
operating systems existed during the second generation and were then available
to a wider (but still very select) audience.

I have fond memories of the Bendix G-15 (paper tape) and the IBM 1620 (cards;
typewriter; decimal). During the short time you had the machine, it was truly
a personal computer.

### 1.2.2 The Second Generation (1955-65): Transitors and Batch Systems

Many jobs were batched together, but the systems were still **uniprogrammed**,
a job once started was run to completion without interruption and then flushed
from the system.

A change from the previous generation is that the OS was not reloaded for each
job and hence needed to be protected from the user's execution. As mentioned
above, in the first generation, the beginning of a job contained the trivial
OS-like support features used.

The batches of user jobs were prepared offline (cards to magnetic tape) using
a separate computer (an IBM 1401 with a 1402 card reader/punch). The tape was
brought to the main computer (an IBM 7090/7094) where the output to be printed
was written on another tape. This tape went back to the service machine (1401)
and was printed (on a 1403).

### 1.2.3 The Third Generation (1965-1980): ICs and Multiprogramming

In my opinion Multiprogramming is the biggest change from the OS point of
view. It is with multiprogramming (many processes executing concurrently) that
we have the operating system fielding requests whose arrival order is non-
deterministic. At this point operating systems become notoriously hard to get
right due to the inability to test a significant percentage of the possible
interactions and the inability to reproduce bugs on request.

Since multiple jobs are in memory at the same jobs, one job's memory must be
protected from the other jobs.

#### The Purpose of Multiprogramming

The purpose of multiprogramming is to overlap CPU and I/O activity and thus
greatly improve CPU utilization. Recall that these computers, in particular
the processors, were very expensive.

#### Multiple Batch Streams

  * IBM OS/MFT (Multiprogramming with a Fixed number of Tasks). 
    * OS for IBM system 360.
    * The (real) memory is partitioned and a batch is assigned to a fixed partition.
    * The memory assigned to a partition does not change.
    * Jobs are queued for a specific partition. These jobs are **not** multiprogrammed: When a job is loaded into a partition, it stays there until completion, other jobs destined for that partition wait their turn.
    * Jobs residing in **separate** partitions **are** multiprogrammed. When a job residing in one partition starts a (slow) I/O, the CPU switches to executing a job in another partition.
    * Jobs were **spooled** from cards into the memory; similarly output was spooled from the memory to a printer.
    * More details are presented later, when we study memory management.
  * IBM OS/MVT (Multiprogramming with a Variable number of Tasks) (then other names). 
    * Each job gets just the amount of memory it needs. That is, the partitioning of memory changes as jobs enter and leave.
    * MVT is a more efficient user of resources, but is more difficult to implement.
    * Later, when we study OS/MVT in more detail, we will see that, with varying size partitions, questions such as compaction, holes, and fragmentation arise.

#### Spooling

With multiprogramming, one job could be loading (from say cards), another job
could be printing, and a third computing. So when a card deck was submitted by
the user it could be read directly into an on-disk queue. Then when the system
is ready to run another job, it is already there. Similarly, jobs would print
to disk and later another task would really print these disk files onto paper.

#### Time Sharing

This is multiprogramming with rapid switching between jobs (processes) so
that, to the user it appears that their job is always running (but at a slower
rate). Also individual users spool their own printed output onto a remote
terminal. Deciding when to switch and which process to switch to is called
**scheduling**.

We will study scheduling when we cover processor management a few weeks from
now.

MIT and Dartmouth were pioneers in timesharing. Since I went to MIT, I
naturally believe MIT was first. In particular, during my second semester
(jan-may 1964), I took a course that by luck was chosen to the first one on
the MIT timesharing system CTSS. I do believe that I was in the first group of
undergraduates (about 15 or 20 students I guess) to use timesharing. Tanenbaum
also asserts that MIT was first, but again he was a student there (in
physics).

### 1.2.4 The Fourth Generation (1980-Present): Personal Computers

Serious PC Operating systems such as Unix/Linux, Windows NT/2000/XP/Vista/etc
and (the newer versions of) MacOS are multiprogrammed.

GUIs have become important. What is not clear is whether the GUI should be
part of the kernel.

Early PC operating systems were uniprogrammed and their direct descendants
lasted for quite some time (e.g., Windows ME), but now all (non-embedded) OS
are multiprogrammed.

**Note**: I very much recommend reading all of 1.2, not for this course especially, but for general interest. Tanenbaum writes well and is my age so lived through much of the history himself.

**Homework:**

  * What is multiprogramming?
  * Why was timesharing not widespread on second generation computers?
  * What is spooling? Do you think that advanced personal computers will have spooling as a standard feature in the future?
  * 5\. On early computers, every byte of data read or written was handled by the CPU (i.e., there was no DMA). What implications does this have for multiprogramming?

### 1.2.5 The Fifth Generation (1990-Present): Mobile Computers

Primarily hardware changes.

## 1.3 Computer Hardware Review

  
![system-dia](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/system-
dia.png)

The picture above is very simplified. (For one thing, today separate buses are
used to Memory and Video.)

A **bus** is a set of wires that connect two or more devices. Only one message
can be on the bus at a time. All the devices receive the message: There are no
switches in between to steer the message to the desired destination, but often
some of the wires form an address that indicates which devices should actually
process the message.

### 1.3.1 Processors

Only at a few points will we need to understand the various processor
registers such as the _program counter_ (a.k.a, _instruction pointer_), the
_stack pointer_, and the _Program Status Words (PSWs)_. We will ignore
computer design issues such as _pipelining_ and _superscalar_.

Many of these issues are mentioned in 201 and nearly all of them are covered
in 436, the computer architecture elective.

We do, however, need the notion of a **trap**, that is an instruction that
_atomically_ switches the processor into privileged mode and jumps to a pre-
defined physical address. This is the key for _system calls_ in which a user
program enters the operating system. We will have much more to say about traps
at the end of this chapter.

#### Multithreaded and Multicore Chips

Many of the OS issues introduced by multi-processors of any flavor are also
found in a uni-processor, multi-programmed system. In particular, successfully
handling the concurrency offered by the second class of systems, goes a long
way toward preparing for the first class. The remaining multi-processor issues
are not covered in this course.

### 1.3.2 Memory

We will ignore caches (which are covered in 201 and especially 436; you can
see my online class notes for the latter, if you are interested), but we will
later discuss demand paging, which is very similar. Despite their similarity,
demand paging and caches use largely disjoint terminology. In both cases, the
goal is to combine large, slow memory with small, fast memory to achieve the
effect of large, fast memory.

The central memory in a system is called **RAM** (Random Access Memory). A key
point is that it is volatile, i.e. the memory loses its data if power is
turned off.

#### ROM / PROM / EPROM / EEPROM / Flash Ram

**ROM** (Read Only Memory) is used for (low-level control) software that often comes with devices on general purpose computers, and for the entire software system on non-user-programmable devices such as microwaves and dumb wristwatches. It is also used for non-changing data. A modern, familiar ROM is CD-ROM (or the denser DVD, or the even denser Blu-ray). ROM is non-volatile.

But often this unchangable data needs to be changed (e.g., to fix bugs). This
gives rise first to **PROM** (Programmable ROM), which, like a CD-R, can be
written once (as opposed to being mass produced already written like a CD-
ROM), and then to **EPROM** (Erasable PROM), which is like a CD-RW. Early
EPROMs needed UV light for erasure; **EEPROM**, Electrically EPROM or **Flash
RAM)** can be erased by normal circuitry, which is much more convenient.

#### Memory Protection and Context Switching

As mentioned above when discussing OS/MFT and OS/MVT, multiprogramming
requires that we protect one process from another. That is, we need to
translate the **virtual addresses** (a virtual address is the address as
written in the program) into **physical addresses** (a physical address is the
actual memory address in the computer) such that, at any point in time, the
physical address of each process are disjoint. The hardware that performs this
translation is called the **MMU** or **Memory Management Unit**. (There are
occasions when two processes wish to share memory.)

Note the similarity between (1) translating virtual to physical addresses by
the OS and (2) relocating relative addresses (into absolute addresses) in your
lab 1 linker.

When **context switching** from one process to another, the translation must
change, which can be an expensive operation.

### 1.3.3 Disks

When we do I/O for real, I will show a real disk opened up and illustrate the
components

  * Platter
  * Surface
  * Head
  * Track
  * Sector
  * Cylinder
  * Seek time
  * Rotational latency
  * Transfer time

Devices are often quite difficult to manage and a separate computer, called a
controller, is used to translate OS commands into what the device requires.

#### Solid State Disks (SSDs)

This is flash RAM organized in sector-like blocks as is a disk. Unlike RAM,
SSD is non volatile; unlike a disk it has no moving parts (and so is faster).
The blocks can be written a large number of times. However, the large number
is not large enough to be completely ignored.

### 1.3.A Tapes

The bottom of the memory hierarchy, tapes have large capacities, tiny cost per
byte, and very long access times. Tapes are becoming less important since
their technology improvement has not kept up with the improvement in disks. We
will not study tapes in this course.

### 1.3.4 I/O Devices

In addition to the disks and tapes just mentioned, I/O devices include
monitors (and graphics controllers), NICs (Network Interface Controllers),
Modems, Keyboards, Mice, etc.

The OS communicates with the device controller, not with the device itself.
For each different controller, a corresponding **device driver** is included
in the OS. Note that, for example, many graphics controllers are capable of
controlling a standard monitor, and hence the OS needs many graphics device
drivers.

In theory any SCSI (Small Computer System Interconnect) controller can control
any SCSI disk. In practice this is not true as SCSI gets inproved to wide
scsi, ultra scsi, etc. The newer controllers can still control the older disks
and often the newer disks can run in degraded mode with an older controller.

#### How Does the OS Know When the I/O Is Complete?

Three methods are employed.

  1. The OS can **busy wait**, constantly asking the controller if the I/O is complete. This is the easiest method, but can have low performance. It is also called **polling** or **PIO (Programmed I/O)**.
  2. The OS can tell the controller to start the I/O and then switch to other tasks. The controller must then **interrupt** the OS when the I/O is done. This method induces less waiting, but is harder to program (concurrency!). Moreover, on modern processors a single interrupt is rather costly, much more costly than a single memory reference, but much, much less costly than a disk I/O.
  3. Some controllers can do **DMA (Direct Memory Access)** in which case they deal directly with memory after being started by the CPU. A DMA controller relieves the CPU of some work and halves the number of bus accesses.

We discuss these alternatives more in chapter 5. In particular, we explain the
last point about halving bus accesses.

![1840chipset](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/i840chipset.
png)

### 1.3.6 Buses

On the right is a figure showing the specifications for an Intel chip set
introduced in 2000. The terminology used is not standardized, e.g., hubs are
often called bridges. Most likely due to their location on the diagram to the
right, the Memory Controller Hub is often called the Northbridge and the I/O
Controller Hub the Southbridge.

As shown on the right this chip set has two different width PCI buses. This
particular chip set supplies USB. An alternative is to have a PCI USB
controller.

Unlike the situation in the previous diagram with a single bus, now several
pairs of components can be communicating simultaneously, giving a significant
improvement in performance (and complexity).

### 1.3.7 Booting the Computer

When the power button is pressed, control starts at the BIOS, a PROM
(typically flash) in the system. Control is then passed to (the tiny program
stored in) the MBR (Master Boot Record), which is the first 512-byte block on
the primary disk. Control then proceeds to the first block in the active
partition and from there the OS is finally invoked (normally via an OS
loader).

The above assumes that the boot medium selected by the bios was the hard disk.
Other possibilities include a CD-ROM or the network.

## 1.4 OS Zoo

There is not much difference between mainframe, server, multiprocessor, and PC
OS's. Indeed the 3e considerably softened the differences given in the 2e and
this continues in the 4e. For example Unix/Linux and Windows runs on all of
them.

This course covers all four of those classes, which perhaps should be
considered just one class .

### 1.4.1 Mainframe Operating Systems

Used in data centers, these systems ofter tremendous I/O capabilities and
extensive fault tolerance.

### 1.4.2 Server Operating Systems

Perhaps the most important servers today are web servers. Again I/O (and
network) performance are critical.

### 1.4.3 Multiprocessor Operating systems

A multiprocessor (as opposed to a multi-computer or multiple computers or
computer network or grid) means multiple processors sharing memory and
controlled by a single instance of the OS, which typically can run on any of
the processors. Often it can run on several simultaneously.

Multiprocessors existed almost from the beginning of the computer age, but now
are not exotic. Indeed, even my current laptop is a multiprocessor.

#### Multiple computers

The operating system(s) controlling a system of multiple computers often are
classified as either a _Network OS_ or a _Distributed OS_. The former is
basically a collection of ordinary PCs on a LAN that use the network
facilities available on PC operating systems. Some extra utilities are often
present to ease running jobs on remote processors.

A _Distributed OS_ is a more sophisticated and seamless version of the above
where the boundaries between the processors are made nearly invisible to users
(except for performance).

This subject is not part of our course (but often is covered in 2251).

### 1.4.4 PC Operating Systems

In the recent past some OS systems (e.g., ME) were claimed to be _tailored_ to
client operation. Others felt that they were _restricted_ to client operation.
This seems to be gone now; a modern PC OS is fully functional. I guess for
marketing reasons some of the functionality can be disabled.

### 1.4.5 Handheld Computer Operating Systems

This includes phones.

The only real difference between this class and the above is the restriction
to very modest memory and very low power. However, the very modest memory
keeps getting bigger and some phones now include a stripped-down linux.

### 1.4.6 Embedded Operating Systems

The OS is part of the device, e.g., microwave ovens, and cardiac monitors. The
OS is on a ROM so is not changed.

Since no user code is run, protection is not as important. In that respect the
OS is similar to the very earliest computers. Embedded OS are very important
commercially, but not covered much in this course.

### 1.4.7 Sensor Node Operating Systems

These are embedded systems that also contain sensors and communication devices
so that the systems in an area can cooperate.

### 1.4.8 Real-time Operating Systems

As the name suggests, time (more accurately timeliness) is an important
consideration. There are two classes: soft vs hard real time. In the latter,
missing a deadline is a fatal error--sometimes literally. Very important
commercially, but not covered much in this course.

### 1.4.9 Smart Card Operating Systems

Very limited in power (both meanings of the word).

**Remark**: Professor Marsha Berger, the department's director of undergraduate studies personally told me to mention in my classes that last academic year she had to refer 45 students to the dean for problems with academic integrity. As I mentioned before the department is **very** serious about this subject.

Start Lecture #3

## 1.5 Operating System Concepts

This will be very brief. Much of the rest of the course will consist of
filling in the details.

### 1.5.1 Processes

A _process_ is program in execution. If you run the same program twice, you
have created two processes. For example if you have two programs compiling in
two windows, each instance of the compiler is a separate process.

Often one distinguishes the state or context of a process--its address space
(roughly its memory image), open files, etc.--from the thread of control. If
one has many _threads_ running in the same _task_, the result is a
multithreaded processes.

The OS keeps information about all processes in the **process table**. Indeed,
the OS views the process **as** the entry. This is an example of an active
entity being viewed as a data structure (cf. discrete event simulations), an
observation I first encountered in the (out of print) OS textbook by Finkel I
mentioned previously.

The data contained in a process table entry has many uses. For example, it
enables a processes that is currently blocked or suspended to resume execution
in the future.

![process-tree](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/process-
tree.png)

#### The Process Tree

The set of processes forms a tree via the fork system call. The forker is the
**parent** of the forkee, which is called a **child**. If the system always
blocks the parent until the child finishes, the tree is quite simple, just a
line.

However, in modern OSes, the parent is free to continue executing and in
particular is free to fork again, thereby producing another child. This
produces a process tree as shown on the far right.

A process can send a **signal** to another process to cause the latter to
execute a predefined function (the signal handler). It can be tricky to write
a program with a signal handler since the programmer does not know when in the
mainline program the signal handler will be invoked.

Each user is assigned a User IDentification (**UID**) and all processes
created by that user have this UID. A child has the same UID as its parent. It
is sometimes possible to change the UID of a running process. A group of users
can be formed and given a Group IDentification, **GID**. One UID is special
(the **superuser** or **administrator**) and has extra privileges.

Access to files and devices can be limited to a given UID or GID.

#### Deadlocks

A set of processes is _deadlocked_ if each of the processes is blocked by a
process in the set. The automotive equivalent, shown below, is called
gridlock. (The photograph was sent to me by Laurent Laor, a former 2250
student.)

![deadlock](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/deadlock-
shrink.png)  
![gridlock](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/gridlock-crop-
shrink.png)

### 1.5.2 Address Spaces

Clearly, each process requires memory, but there are other issues as well. For
example, your linkers (will) produce a load module that assumes the process is
loaded at location 0. The result is that every load module has the same
(virtual) address space. The operating system must ensure that the virtual
addresses of concurrently executing processes are assigned disjoint physical
memory.

For another example note that current operating systems permit _each_ process
to be given _more_ (**virtual**) memory than the _total_ amount of (**real**)
memory on the machine.

### 1.5.3 Files

Modern systems have a hierarchy of files. A file system tree.

  * In MSDOS the hierarchy is a forest not a tree. There is no file, or directory that is an ancestor of both a:\ and c:\.
  * In Unix all files are descendants of the root. I suspect this is true of MacOS, which is Unix on the inside.
  * In recent versions of Windows, My Computer looks like the parent of a:\ and c:\, but that is a feature of the UI not the file systems.
  * In Unix the existence of (hard) links weakens the tree to a DAG (directed acyclic graph).
  * Unix also has symbolic links, which when used indiscriminately, permit directed cycles (i.e., the result is not a DAG).
  * Windows has shortcuts, which are somewhat similar to symbolic links.

You can name a file via an **absolute path** starting at the root directory
(or in Windows a root directory) or via a **relative path** starting at the
**current working directory**. One consequence is that the OS must know the
current working directory for each process.

In addition to regular files and directories, Unix also uses the file system
namespace for devices (called **special files**), which are typically found in
the /dev directory. That is, in some ways you can treat the device _as_ a
file. In particular some utilities that are normally applied to (ordinary)
files can be applied as well to some special files. For example, when you are
accessing a unix system using a mouse, type the following command  
`cat /dev/mouse`  
and then move the mouse. On my more modern system the command is  
`cat /dev/input/mice`  
You kill the cat (sorry) by typing cntl-C. I tried this on my linux box (using
a text console) and no damage occurred. Your mileage may vary.

Before a file can be accessed, it is normally **opened** and a file descriptor
obtained. Subsequent I/O system calls (e.g., read and write) use the file
descriptor rather that the file name. This is an optimization that enables the
OS to find the file once and save the information in a file table accessed by
the file descriptor.

Many systems have standard files that are automatically made available to a
process upon startup. These (initial) file descriptors are fixed.

  * standard input: fd=0
  * standard output: fd=1
  * standard error: fd=2

A convenience offered by some command interpreters is a pipe or pipeline. For
example the following command, which pipes the output of dir into a
character/word/line counter, will give the number of files in the directory.

    
    
      dir | wc -w
    

### 1.5.4 Input/Output

There are a wide variety of I/O devices that the OS must manage. Some of these
require special treatment; for example, if two processes are printing at the
same time, the OS must _not_ interleave the output.

The OS contains device specific code (drivers) for each device (really each
controller) as well as device-independent I/O code.

### 1.5.5 Protection

Files and directories have associated permissions.

  * Most systems supply at least rwx (readable, writable, executable).
  * Separate permissions can be defined for the file's owner (files, like processes and users, have UIDs and GIDs), for other users with the same GID as the file, and for everyone else.
  * When a file is opened, permissions are checked and, if the open is permitted, a file descriptor is returned that is used for subsequent operations.
  * A more general mechanism is to provide an **access control list** for each file.
  * Often files have attributes as well. For example the linux ext2 and ext3 file systems support a d attribute that is a hint to the dump program not to backup this file.

Memory assigned to a process, i.e., an address space, must also be protected
so that unrelated processes do not read and write each others' memory.

#### Security

Security has of course sadly become a very serious concern. The topic is quite
deep and I do not feel that the necessarily superficial coverage that time
would permit is useful so we are not covering the topic at all.

### 1.5.6 The Shell (or Command Interpreter)

The shell presents the command line interface to the operating system and
offers several convenient features.

  * Invoke commands.
  * Pass arguments to the commands.
  * Redirect the output of a command to a file or device.
  * Redirect the input of a command to be from a file or device.
  * Pipe one command to another (as illustrated above via dir | wc).

Instead of a shell, one can have a more graphical interface.

### 1.5.7 Ontogeny Recapitulates Phylogeny

Some concepts become obsolete and then reemerge due in both cases to
technology changes. Several examples follow. Perhaps the cycle will repeat
with smart card OS.

#### Large Memories (and Assembly Language)

The use of assembly languages greatly decreases when memories get larger. When
minicomputers and microcomputers (early PCs) were first introduced, they each
had small memories and for a while assembly language again became popular.

#### Protection Hardware (and Monoprogramming)

Multiprogramming requires protection hardware. Once the hardware becomes
available monoprogramming becomes obsolete. Again when minicomputers and
microcomputers were introduced, they had no such hardware so monoprogramming
revived.

#### Disks (and Flat File Systems)

When disks are small, they hold few files and a flat (single directory) file
system is adequate. Once disks get large a hierarchical file system is
necessary. When mini and microcomputer were introduced, they had tiny disks
and the corresponding file systems were flat.

#### Virtual Memory (and Dynamically Linked Libraries)

Virtual memory, discussed in great detail later, permits a single program to
address more memory than present in the computer (the latter is called
physical memory). The ability to dynamically remap address also permits
programs to link to libraries during runtime. Hence, when VM hardware becomes
available, so does dynamic linking.

**Homework:** 12.

![components](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/components.pn
g)

## 1.6 System Calls

A **System call** is the mechanism by which a user (i.e., a process running in
user mode) directly interfaces with the OS. Some textbooks use the term
_envelope_ for the component of the OS responsible for fielding system calls
and _dispatching_ them to the appropriate component of the OS. On the right is
a picture showing some of the OS components and the external events for which
they are the interface.

Note that the OS serves two masters. The hardware (at the bottom)
_asynchronously_ sends interrupts and the user (at the top) _synchronously_
invokes system calls and generates page faults.

There is an important difference between these two cases.

  * When the user issues a system call or generates a page fault, the operating system is not executing. When the operating system last relinquished control, it had the opportunity to prepare itself for processing a system call or a page fault.
  * In contrast at almost any point during execution, an interrupt can transfer control to a given point in the operating system. This means that at (almost) any point during its execution, the OS must be prepared for an immediate transfer to a driver or the scheduler. Since the code being executed just prior to the interrupt might be using variables shared with the drivers and the scheduler, being prepared for this immediate transfer is not always easy. 

### 1.6.A Executing a System Call

What happens when a user executes a system call such as read()? We show a
detailed picture below, but at a high level, the following actions occur.

  1. Normal function call (in C, Ada, Python, Java, etc.).
  2. Library routine (probably in C, or similar, language).
  3. Small assembler routine. 
    1. Move arguments to a predefined place (perhaps registers).
    2. Poof (a trap instruction) and then the OS proper runs in supervisor mode.
    3. Fix up result (move it to the correct place).
  4. The library routine returns.

#### A Method Call and the Runtime Stack

![sinX](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/sinX.png)

Before considering the read() system call, it might be good to review a
typical call/return sequence for a more familiar method. On the right we see
the assembler-like instructions that would appear when one method invokes
sin(x).

The numbers on the left represent memory locations. As we did in the linker
lab, the machine is word addressable and each instruction occupies one word.
The sin() method is in words 1041-1102 and the caller is from 40-300. We are
interested only in the call itself, which occupies 59-61.

The problems we need to solve are first to transfer control from the caller to
the callee passing the value of x and second to transfer control back
returning the calculated value of sin(x).

The key data structure is a run-time stack whose changing contents we will
show on the board.

  1. The first instruction (in word 59) pushes the value of x on the stack.
  2. Next we jump to sin() and save the next address (where to save it is system dependent).
  3. Now we calculate sin and put the result in register 1 (the assumed protocol for returning a value).
  4. Then we jump to the address previously saved.
  5. We are now back in the caller. The next instruction increments the stack pointer, which effectively removes the value of x from the stack. Note that now, after the call and return, the stack is back the condition it had when we began.

#### The read() System Call

![syscall](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/syscall.png)

A typical invocation of the (Unix) read system call is:

    
    
      count = read(fd,buffer,nbytes)
    

This invocation reads up to nbytes from the file specified by the file
descriptor fd into the character array buffer. The actual number of bytes read
is returned (it might be less than nbytes if, for example, an end-of-file was
encountered). In more detail, the steps performed are as follows.

  1. Push the third parameter on the stack.
  2. Push the second parameter on the stack.
  3. Push the first parameter on the stack.
  4. Call the library routine, which involves saving the return address and jumping to the routine.
  5. Machine/OS dependent actions, for example putting the system call number for read in a well defined place, such as a specific register. This requires assembly language.
  6. Trap (a magic instruction) causes control to enter the operating system proper and shifts the computer to privileged mode. Assembly language is again used.
  7. The envelope uses the system call number to access a table of pointers to find the handler for this system call.
  8. The read system call handler processes the request.
  9. Another magic (assembler language) instruction returns to user mode and jumps to the location right after the trap.
  10. The library routine returns (there is more; e.g., the count must be returned).
  11. The stack is popped (ending the function invocation of read).

A major complication is that the system call handler may block. Indeed, the
read system call handler is likely to block. In that case a the operating
system will probably switch to another process. Such process switching is far
from trivial and is discussed later in the course.

### 1.6.1 System Calls for Process Management

A Few Important Posix/Unix/Linux and Win32 System Calls

PosixWin32Description

Process Management

Fork

CreateProcess

Clone current process

exec(ve)

Replace current process

wait(pid)

WaitForSingleObject

Wait for a child to terminate.

exit

ExitProcess

Terminate process & return status

File Management

open

CreateFile

Open a file & return descriptor

close

CloseHandle

Close an open file

read

ReadFile

Read from file to buffer

write

WriteFile

Write from buffer to file

lseek

SetFilePointer

Move file pointer

stat

GetFileAttributesEx

Get status info

Directory and File System Management

mkdir

CreateDirectory

Create new directory

rmdir

RemoveDirectory

Remove _empty_ directory

link

(none)

Create a directory entry

unlink

DeleteFile

Remove a directory entry

mount

(none)

Mount a file system

umount

(none)

Unmount a file system

Miscellaneous

chdir

SetCurrentDirectory

Change the current working directory

chmod

(none)

Change permissions on a file

kill

(none)

Send a signal to a process

time

GetLocalTime

Elapsed time since 1 jan 1970

We describe very briefly some of the Unix (Posix) system calls. A short
description of the Windows interface is in the book.

To show how the four process management calls enable much of process
management, consider the following highly simplified shell.

    
    
      while (true)
         display_prompt()
         read_command(command)
         if (fork() != 0)
            waitpid(...)
         else
            execve(command)
         endif
      endwhile
    

The fork() system call duplicates the process. That is we now have a second
process, which is a child of the process that actually executed the fork().
The parent and child are very, VERY nearly identical. For example they have
the same instructions, they have the same data, and they are both currently
executing the fork() system call.

But there is a difference!

The fork() system call returns a zero in the child process and returns a
positive integer in the parent. In fact the value returned to the parent is
the PID (process ID) of the child.

Thus, the parent and child execute different branches of the if-then-else in
the code above.

Note that simply removing the waitpid(...) gives background jobs.

### 1.6.2 System Calls for File Management

Most files are accessed sequentially from beginning to end. In this case the
operations performed are  
    open()     \-- possibly creating the file  
    multiple read()s and write()s  
    close()

For non-sequential access, lseek is used to move the File Pointer, which is
the location in the file where the next read or write will take place.

![mount](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/mount.png)

### 1.6.3 System Calls for Directory Management

Directories are created and destroyed by mkdir and rmdir. Directories are
changed by the creation, modification, and deletion of files. As mentioned,
open can create files. Files can have several names: link gives another name
to an existing file and unlink removes a name. When the last name is gone (and
the file is no longer open by any process), the file data is destroyed.

In Unix, one file system can be **mounted** on (attached to) another. When
this is done, access to an existing directory on the second filesystem is
temporarily replaced by the entire first file system. Most often the directory
chosen is empty before the mount so no files become (temporarily) invisible.

The top picture shows two file systems; the second row shows the result when
the right hand file system is mounted on /y. In both cases squares represent
directories and circles represent regular files.

This is how a Unix system can enable all files, even those on different
physical disks and using different filesystems, to be descendants of a single
root

### 1.6.4 Miscellaneous System Calls

Skipped

### 1.6.5 The Windows Win32 API

Skipped

## 1.A Addendum on Transfer of Control

The transfer of control between user processes and the operating system kernel
can be quite complicated, especially in the case of blocking system calls,
hardware interrupts, and page faults. Before tackling these issues later, we
begin with the familiar example of a procedure call within a user-mode
process.

An important OS objective is that, even in the more complicated cases of page
faults and blocking system calls requiring device interrupts, simple procedure
call semantics are observed _from a user process viewpoint_. The complexity is
hidden inside the kernel itself, yet another example of the operating system
providing a more abstract, i.e., simpler, virtual machine to the user
processes.

More details will be added when we study memory management (and know
officially about page faults) and more again when we study I/O (and know
officially about device interrupts).

A number of the points below are far from standardized. Such items as where to
place parameters, which routine saves the registers, exact semantics of trap,
etc, vary as one changes language/compiler/OS. Indeed some of these are
referred to as calling conventions, i.e. their implementation is a matter of
convention rather than logical requirement. The presentation below is, we
hope, reasonable, but must be viewed as a generic description of what could
happen, rather than a real description of what does happen with, say, C
compiled by the Microsoft compiler running on Windows 7.

### 1.A.1 User-mode Procedure Calls

Procedure f calls g(a,b,c) in process P. An example is above where a user
program calls read(fd,buffer,nbytes). Note that both f() and g() are in the
same process P and no action goes outside P. Thus we will not mention the
process again in this description.

#### Actions by f Prior to the Call

  1. Save the registers by pushing them onto the stack  (in some implementations this is done by g instead of by f) .  
  

  2. Push arguments c,b,a onto P's stack.  

Note: Stacks usually grow downward from the top of P's segment, so pushing an
item onto the stack actually involves decrementing the stack pointer, SP.  
Note: Some compilers store arguments in registers not on the stack.

#### Executing the Call Itself

  3. Execute METHODJUMP <start-address of g>.  
This (fictitious) instruction saves the program counter PC (a.k.a. the
instruction pointer IP), and jumps to the start address of g.

The value saved is actually the updated program counter, i.e., the location of
the next instruction (the instruction to be executed by f when g returns).

#### Actions by g upon Being Called

  4. Allocate space for g's local variables by suitably decrementing SP.  
  

  5. Start execution from the beginning of the program, referencing the parameters as needed. The execution may involve calling other procedures, possibly including recursive calls to f and/or g.

#### Actions by g When Returning to f

  6. If g is to return a value, store it in the conventional place.  
  

  7. Undo step 4: Deallocate local variables by incrementing SP.  
  

  8. Undo step 3: Execute RETURN (another fictitious instruction), i.e., pop the stack and set PC to the value popped, which is the return address pushed in step 4.

#### Actions by f upon the Return from g:

  9. (We are now at the instruction in f immediately following the call to g.)  
Undo step 2: Remove the arguments from the stack by incrementing SP.  
  

  10. Undo step 1: Restore the registers while popping their values off the stack.  
  

  11. Continue the execution of f, referencing the returned value of g, if any.

#### Properties of (User-Mode) Procedure Calls

  * Predictable (often called synchronous) behavior: The author of f knows where and hence when the call to g will occur. There are no surprises, so it is relatively easy for the programmer to ensure that f is prepared for the transfer of control.
  * LIFO (stack-like) structure of control transfer: we can be sure that control will return to f() when the call to g() exits. The above statement holds even if g() calls h() and then h() calls d(). In fact it even holds if, via recursion, g() calls f().  We are ignoring language features such as throwing and catching exceptions, and the use of unstructured assembly coding. In the latter cases all bets are off.
  * Everything happens entirely in user mode and user space.

### 1.A.2 Kernel-mode procedure calls

We mean one procedure running in kernel mode calling another procedure, which
will also be run in kernel mode. Later, we will discuss switching from user
mode to kernel mode and back.

There is not much difference between the actions taken during a kernel-mode
procedure call and during a user-mode procedure call. The procedures executing
in kernel-mode are permitted to issue privileged instructions, but the
instructions used for transferring control are all unprivileged so there is no
change in that respect.

One difference is that often a different stack is used in kernel mode, but
that simply means that the stack pointer must be set to the kernel stack when
switching from user to kernel mode. But we are not switching modes in this
section; the stack pointer already points to the kernel stack. Often there are
two stack pointers one for kernel mode and one for user mode.

### 1.A.3 The Trap instruction

The trap instruction, like a procedure call, is a synchronous transfer of
control: We can see where, and hence when, it is executed. In this respect,
there are no surprises. Although not surprising, the trap instruction does
have an unusual effect: processor execution is switched from user-mode to
kernel-mode. That is, the trap instruction normally is itself executed in
user-mode (it is naturally an _UN_privileged instruction), but the next
instruction executed (which is _NOT_ the instruction written after the trap)
is executed in kernel-mode.

Process P, running in unprivileged (user) mode, executes a trap. The code
being executed is written in assembler since there are no high level languages
that generate a trap instruction. There is no need to name the function that
is executing. Compare the following example to the explanation of f calls g
given above.

#### Actions by P prior to the trap

  1. Save the registers by pushing them onto the stack.  
  

  2. Store any arguments that are to be passed.  The stack is not normally used to store these arguments since the kernel has a different stack. Often registers are used. 

#### Executing the trap itself

  3. Execute TRAP <trap-number>.  
This instruction switch the processor to kernel (privileged) mode, jumps to a
location in the OS determined by trap-number, and saves the return address.
For example, the processor may be designed so that the next instruction
executed after a trap is at physical address 8 times the trap-number.  
The trap-number can be thought of as the name of the code-sequence to which
the processor will jump rather than as an argument to trap.

#### Actions by the OS upon being TRAPped into

  4. Jump to the real code.  
Recall that trap instructions with different trap numbers jump to locations
very close to each other. There is not enough room between them for the real
trap handler. Indeed one can think of the trap as having an extra level of
indirection; it jumps to a location that then jumps to the real start address.
If you learned about writing jump tables in assembler, this is very similar.  
  

  5. Check all arguments passed. The kernel must be paranoid and assume that the authors of the user mode program wear black hats.  
  

  6. Allocate space by decrementing the kernel stack pointer.  
The kernel and user stacks are separate.  
  

  7. Start execution from the jumped-to location.

#### Actions by the OS when returning to user mode

  8. Undo step 6: Deallocate space by incrementing the kernel stack pointer.  
  

  9. Undo step 3: Execute (in assembler) another special instruction, RTI or ReTurn from Interrupt, which returns the processor to user mode and transfers control to the return location saved by the trap. The word interrupt appears because an RTI is also used when the kernel is returning from an interrupt as well as the present case when it is returning from an trap. Actually, an RTI doesn't always go back to user mode. Instead it returns to the mode before the trap or interrupt.

#### Actions by P upon the return from the OS

  10. We are now in at the instruction right after the trap  
Undo step 1: Restore the registers by popping the stack.  
  

  11. Continue the execution of P, referencing the returned value(s) of the trap, if any.

####  Properties of TRAP/RTI

  * Synchronous behavior: The author of the assembly code in P knows where and hence when the trap will occur. There are no surprises, so it is relatively easy for the programmer to prepare for the transfer of control.
  * Trivial control transfer _when viewed from P_: The next instruction _of P_ that will be executed is the one following the trap. As we shall see later, other processes may execute between P's trap and the next P instruction.
  * Starts and ends in user mode and user space, but executed in kernel mode and kernel space in the middle.

**Note:** A good way to use the material in the addendum is to compare the first case (user-mode f calls user-mode g) to the TRAP/RTI case line by line so that you can see the similarities and differences.

Start Lecture #4

## 1.7 Operating System Structure

I must note that Tanenbaum is a big advocate of the so called microkernel
approach in which as much as possible is moved out of the (supervisor mode)
kernel into separate processes. The (hopefully small) portion left in
supervisor mode is called a microkernel.

In the early 90s this was popular. Digital Unix (subsequently called True64)
and Windows NT/2000/XP/Vista/7/8 are examples. Digital Unix was based on Mach,
a research OS from Carnegie Mellon university. Lately, the growing popularity
of Linux has called into question the belief that all new operating systems
will be microkernel based.

### 1.7.1 Monolithic approach

The previous picture: one big program.

The system switches from user mode to kernel mode during the trap and then
back when the OS does an RTI (return from interrupt).

While in supervisor mode, the OS naturally includes procedure calls and
returns.

Modern monolithic systems, such as Windows and Linux, are not completely
monolithic in that during execution, they can load code modules as needed.
This load on demand capability is mainly used for device drivers.

We can structure the system better than above might suggest, which brings us
to ...

![layers](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/layers.png)

### 1.7.2 Layered Systems

Some systems have more layers and are more strictly structured.

An early layered system was THE operating system by Dijkstra and his students
at Technische Hogeschool Eindhoven. This was a simple batch system so the
operator was the user.

The actual layers were

  1. The operator process
  2. User programs
  3. I/O mgt
  4. Operator console--process communication
  5. Memory and drum management

The layering was done by convention, i.e. there was no enforcement by hardware
and the entire OS is linked together as one program. This is true of many
modern OS systems as well (e.g., linux).

The MULTICS system was layered in a more formal manner. The hardware provided
several protection layers and the OS used them. That is, arbitrary code could
not jump into or access data in a more protected layer.

### 1.7.3 Microkernels

The idea is to have the kernel, i.e. the portion running in supervisor mode,
as small as possible and to have most of the operating system functionality
provided by separate processes. The _microkernel_ provides just enough to
implement processes.

![microkernel](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/microkernel.
png)

This does have advantages. For example an error in the file server cannot
corrupt memory in the process server since they have separate address spaces
(they are after all separate process). Confining the effect of errors makes
them easier to track down. Also an error in the ethernet driver can corrupt or
stop network communication, but it _cannot_ crash the system as a whole.

But the microkernel approach does mean that when a (real) user process makes a
system call there are more processes switches. These are not free.

Related to microkernels is the idea of putting the mechanism in the kernel,
but not the policy. For example, the kernel would know how to select the
highest priority process and run it, but some external process would assign
the priorities. In this way changing the priority scheme could become a
relatively minor event compared to the situation in monolithic systems where
the entire kernel must be relinked and rebooted.

#### Microkernels Not So Different In Practice

Dennis Ritchie, the inventor of the C programming language and co-inventor,
with Ken Thompson, of Unix was interviewed in February 2003\. The following is
from that interview.

What's your opinion on microkernels vs. monolithic?

> They're not all that different when you actually use them. Micro kernels
tend to be pretty large these days, monolithic kernels with loadable device
drivers are taking up more of the advantages claimed for microkernels.

I should note, however, that Tanenbaum's Minix microkernel (excluding the
processes) _is_ quite small, about 13,000 lines.

### 1.7.4 Client-Server

When implemented on one computer, a client-server OS often uses the
microkernel approach shown above in which the microkernel just handles
communication between clients and servers, and the main OS functions are
provided by a number of separate processes.

A _distributed system_ can be thought of as an extension of the client server
concept where the servers are remote.

![dist-client-server](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/dist-
client-server.png)

The figure on the right would describe a distributed system of yesteryear,
where memory was scarce and it would be considered lavish to have full systems
on each machine.

Today with plentiful memory, each machine would have all the different
servers. So the only reason an OS-internal message would go to another
computer is if the originating process wished to communicate with a specific
process on that computer (for example needed to access a remote disk).

Distributed systems are becoming increasingly important for application
programs. Perhaps the program needs data found only on certain machine (no one
machine has all the data). For example, think of (legal, of course) file
sharing programs.  
  
Distributed systems are also used to reduce the time required by an
application. You do this by dividing the program into pieces, which are run
concurrently on separate computers.

**Homework:** The client-server model is popular in distributed systems. Can it also be used in single-computer system?

### 1.7.5 Virtual Machines

Use a hypervisor (i.e., beyond supervisor, i.e. beyond a normal OS) to switch
between multiple _Operating Systems_. The modern name for a hypervisor is a
Virtual Machine Monitor (VMM).

#### VM/370

![hypervisor](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/hypervisor.pn
g)

The hypervisor idea was made popular by IBM's CP/CMS (now VM/370). CMS stood
for Cambridge Monitor System since it was developed at IBM's Cambridge (MA)
Science Center. It was renamed, with the same acronym (an IBM specialty, cf.
RAID) to Conversational Monitor System.

  * Each App/CMS runs on a _virtual_ 370.
  * CMS is a _single user_ OS.
  * A system call in an App (application) traps to the corresponding CMS.
  * CMS believes it is running on the actual hardware so issues I/O instructions but ...
  * ... I/O instructions in CMS trap to VM/370.
  * This idea is still used but the guest OS is now normally a full-featured operating system rather than a simple system like CMS. For example, the newest IBM systems can run multiple instances of linux as well as multiple instances of traditional IBM Operating Systems on a single hardware platform.

#### Virtual Machines Redicovered

Recently, virtual machine technology has moved to machines (notably x86) that
are not fully virtualizable. Recall that when CMS executed a privileged
instruction, the hardware trapped to the real operating system. On x86,
privileged instructions are _ignored_ when executed in user mode, so running
the guest OS in user mode won't work. Bye bye (traditional) hypervisor. But a
new style emerged where the hypervisor runs, not on the hardware, but on the
host operating system. See the text for a sketch of how this (and another idea
paravirtualization) works. An important research advance was Disco from
Stanford University that led to the successful commercial product VMware.

##### Sanity Restored

Both AMD and Intel have extended the x86 architecture to better support
virtualization. The newest processors produced today (2008) by both companies
now support an additional (higher) privilege mode for the VMM. The guest OS
now runs in the old privileged mode (for which it was designed) and the
hypervisor/VMM runs in the new higher privileged mode from which it is able to
monitor the usage of hardware resources by the guest operating system(s).

#### The Java Virtual Machine

The idea is that a new (rather simple) computer architecture called the Java
Virtual Machine (JVM) was invented but not built (in hardware). Instead,
interpreters for this architecture are implemented in software on many
different hardware platforms. Each interpreter is also called a JVM. The java
compiler transforms java into instructions for this new architecture, which
then can be interpreted on any machine for which a JVM exists.

This has portability as well as security advantages, but at a cost in
performance.

Of course java can also be compiled to native code for a particular hardware
architecture and other languages can be compiled into instructions for a
software-implemented virtual machine (e.g., pascal with its p-code).

### 1.7.6 Exokernels

Similar to VM/CMS but the virtual machines have disjoint resources (e.g.,
distinct disk blocks) so less remapping is needed.

## 1.8 The World According to C

### 1.8.1 The C Language

Assumed knowledge.

### 1.8.2 Header Files

Assumed knowledge.

### 1.8.3 Large Programming Projects

Mostly assumed knowledge. Linker's are very briefly discussed. Our earlier
discussion was much more detailed.

### 1.8.4 The model of Run Time

Extremely brief treatment with only a few points made about the running of the
operating itself.

  * The text (code) segment is normally read only.
  * The stack is initially of size zero; it grows and shrinks as functions are called and return.
  * The data segment is initially not empty, with some of it initialized. It can grow under program control and perhaps can shrink.

## 1.9 Research on Operating Systems

Skipped

## 1.10 Outline of the Rest of this Book

Skipped

## 1.11 Metric Units

Assumed knowledge. Note that what is covered is just the prefixes, i.e. the
names and abbreviations for various powers of 10.

## 1.12 Summary

Skipped, but you should read and be sure you understand it (about 2/3 of a
page).

# Chapter 2 Process and Thread Management

Tanenbaum's chapter title is Processes and Threads. I prefer to add the word
management. The subject matter is processes, threads, scheduling, interrupt
handling, and IPC (Inter-Process Communication--and Coordination).

## 2.1 Processes

**Definition:** A **process** is a program in execution.

  * We are assuming a **multiprogramming** OS that can switch from one process to another.
  * Sometimes this is called _pseudoparallelism_ since one has the illusion of a parallel processor.
  * The other possibility is _real parallelism_ in which two or more processes are actually running at once because the computer system is a parallel processor, i.e., has more than one processor.
  * We do not study real parallelism (parallel processing, distributed systems, multiprocessors, etc) in this course.

### 2.1.1 The Process Model

![multiprogramming](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/multipr
ogramming.png)

Even though in actuality there are many processes running at once, the OS
gives each process the _illusion_ that it is running alone.

#### Virtual Time

Virtual time is the time used by just this processes. Virtual time progresses
at a rate independent of other processes.  (Actually, this is false, the
virtual time is typically incremented a little during the systems calls used
for process switching; so if there are other processes, overhead virtual time
occurs.)

#### Virtual Memory

Virtual memory is the memory as viewed by the process. Each process typically
believes it has a contiguous chunk of memory starting at location zero. Of
course this can't be true of all processes (or they would be using the same
memory) and in modern systems it is actually true of no processes (the memory
assigned to a single process is not contiguous and does not include location
zero).  
  
Think of the individual modules that are input to the linker. Each numbers its
addresses from zero; the linker eventually translates these relative addresses
into absolute addresses. That is the linker provides to the assembler a
virtual memory in which addresses start at zero.

Virtual time and virtual memory are examples of abstractions provided by the
operating system to the user processes so that the latter experiences a more
pleasant virtual machine than actually exists.

**Remark**: Please note that the problem numbers are from the fourth edition. They are not the same problems in older editions.

### 2.1.2 Process Creation

From the users' or external viewpoint there are several mechanisms for
creating a process.

  1. System initialization, including daemon (see below) processes.
  2. Execution of a process creation system call (fork()) by a running process.
  3. A user request to create a new process.
  4. Initiation of a batch job.

But looked at internally, from the system's viewpoint, the second method
dominates. Indeed, in early versions of Unix only one process (called _init_)
is created at system initialization; all the others are created by the
`fork()` system call.

**Question**: Why have init? That is why not have all processes created via method 2?  
**Answer**: Because without init there would be no running process to create any others.

#### Definition of Daemon

Many systems have daemon process lurking around to perform tasks when they are
needed. I was pretty sure the terminology was related to mythology, but didn't
have a reference until a student  found The {Searchable} Jargon Lexicon at
http://developer.syndetic.org/query_jargon.pl?term=demon

> daemon: /day'mn/ or /dee'mn/ n. [from the mythological meaning, later
rationalized as the acronym `Disk And Execution MONitor'] A program that is
not invoked explicitly, but lies dormant waiting for some condition(s) to
occur. The idea is that the perpetrator of the condition need not be aware
that a daemon is lurking (though often a program will commit an action only
because it knows that it will implicitly invoke a daemon). For example, under
ITS (a very early OS), writing a file on the LPT spooler's directory would
invoke the spooling daemon, which would then print the file. The advantage is
that programs wanting (in this example) files printed need neither compete for
access to nor understand any idiosyncrasies of the LPT. They simply enter
their implicit requests and let the daemon decide what to do with them.
Daemons are usually spawned automatically by the system, and may either live
forever or be regenerated at intervals. Daemon and demon are often used
interchangeably, but seem to have distinct connotations. The term `daemon' was
introduced to computing by CTSS people (who pronounced it /dee'mon/) and used
it to refer to what ITS called a dragon; the prototype was a program called
DAEMON that automatically made tape backups of the file system. Although the
meaning and the pronunciation have drifted, we think this glossary reflects
current (2000) usage.

As is often the case, wikipedia.org proved useful. Here is the first paragraph
of a much larger entry. The wikipedia also has entries for other uses of
daemon.

> In Unix and other computer multitasking operating systems, a daemon is a
computer program that runs in the background, rather than under the direct
control of a user; they are usually instantiated as processes. Typically
daemons have names that end with the letter "d"; for example, syslogd is the
daemon which handles the system log.

### 2.1.3 Process Termination

Again from the outside there appear to be several termination mechanism.

  1. Normal exit (voluntary).
  2. Error exit (voluntary).
  3. Fatal error (involuntary).
  4. Killed by another process (involuntary).

And again, internally the situation is simpler. In Unix terminology, there are
two system calls _kill()_ and _exit()_ that are used. kill() (poorly named in
my view) sends a signal to another process. For many types of signals, if the
signal is not caught (via the signal() or sigaction() system call) the process
is terminated. There is also an uncatchable signal. The exit() system call is
used for self termination and can indicate success or failure.

![process-hier](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/process-
hier.png)

### 2.1.4 Process Hierarchies

Modern general purpose operating systems permit a user to create and destroy
processes.

  * In unix this is done by the **fork()** system call, which creates a **child** process, and the **exit** system call, which terminates the current process.
  * After a fork both parent and child keep running (indeed they have the _same_ program text) and each can fork off other processes.
  * A process tree results. The root of the tree is a special process created by the OS during startup.
  * A process can _choose_ to wait for children to terminate. For example, if C issued a wait() system call mentioning G, C would block until G finished.

Old or primitive operating system like MS-DOS are not fully multiprogrammed,
so when one process starts another, the first process is _automatically_
blocked and waits until the second is finished. This implies that the process
tree degenerates into a line.

### 2.1.5 Process States and Transitions

The diagram on the right contains much information. I often include it on
exams.

![process-states](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/process-
states.png)

Consider a running process P that issues an I/O request.

  * The process blocks.
  * At some later point, a disk interrupt occurs and the driver detects that P's request is satisfied.
  * P is unblocked, i.e. is moved from blocked to ready
  * At some later time the operating system scheduler looks for a ready job to run and picks P.

A preemptive scheduler has the dotted line preempt;  
A non-preemptive scheduler doesn't.

The number of processes changes only for two arcs: create and terminate.

Suspend and resume are medium term scheduling.

  * Done on a longer time scale.
  * Involves memory management as well. As a result we study it later.
  * Sometimes called two level scheduling.
![fig-2-3](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/fig-2-3.png)

As mentioned previously, one can organize an OS around the scheduler.

  * Write a minimal kernel (a micro-kernel) consisting of the scheduler, interrupt handlers, and IPC (interprocess communication).
  * The rest of the OS consists of kernel processes (e.g. memory, filesystem) that act as servers for the user processes (which of course act as clients).
  * The system processes also act as clients of other system processes.
  * The above is called the client-server model and is one Tanenbaum likes. His Minix operating system works this way.
  * Indeed, there was reason to believe that the client-server model would dominate OS design. But that hasn't happened.
  * Such an OS is sometimes called _server based_.
  * Systems like traditional Unix or Linux are then called _self-service_ since the user process serves itself. That is, the user process switches to kernel mode (via the TRAP instruction) and performs the system call itself without transferring control to another process.

### 2.1.6 Implementation of Processes

The OS organizes the data about each process in a table naturally called the
**process table**. Each entry in this table is called a **process table
entry** or **process control block**.

Characteristics of the process table.

  * One entry per process.
  * The central data structure for process management.
  * A process state transition (e.g., moving from blocked to ready) is reflected by a change in the value of one or more fields in the process control block.
  * We have converted an active entity (a process) into a data structure (a process control block). Finkel calls this the _level principle_ an active entity becomes a data structure when looked at from a lower level.
  * The process control block contains a great deal of information about the process. For example, 
    * Saved value of registers including the program counter (i.e., the address of the next instruction) when the process not running.
    * Stack pointer.
    * CPU time used.
    * Process id (PID).
    * Process id of parent (PPID).
    * User id (uid.
    * Group id (gid).
    * Pointer to text segment (memory for the instructions).
    * Pointer to data segment.
    * Pointer to stack segment.
    * UMASK (default permissions for new files).
    * Current working directory.
    * Many others.

Start Lecture #5

### 2.1.6A: An Addendum on Interrupts

This should be compared with the addenda on transfer of control and trap.

In a well defined location in memory (specified by the hardware) the OS stores
an **interrupt vector**, which contains the address of the interrupt handler.

  * Tanenbaum calls the interrupt handler the interrupt service routine.
  * Actually one can have different priorities of interrupts and the interrupt vector then contains one pointer for each level. This is why it is called a vector.

Assume a process P is running and a disk interrupt occurs indicating the
completion of a disk read previously issued by process Q, which is currently
blocked. Note that disk interrupts are unlikely to be for the currently
running process (because the process that initiated the disk access is likely
to be blocked).

#### Actions by P Just Prior to the Interrupt:

  1. Who knows??  
This is the difficulty of debugging code depending on interrupts, the
interrupt can occur (almost) anywhere. Thus, we do _not_ know what happened
just before the interrupt.

    * With hardware monitors we _can_ determine what happened for this particular execution.
    * But, if we re-execute the process, the interrupt will likely occur at a different point.
    * Indeed, we do not even know which process P was running when the interrupt occurred (again we can determine this after the fact for one execution, but a re-execution will likely be different).
    * We cannot (even for one specific execution) point to an instruction and say this instruction _caused_ the interrupt.
    * The best we can do is (for one specific execution) point to an instruction and say  this instruction _immediately preceeded_ the interrupt .

#### Executing the interrupt itself:

  2. The hardware saves the program counter and some other registers (or switches to using another set of registers, the exact mechanism is machine dependent).
  3. The hardware finds the address of the interrupt handler in a table and jumps to it.  
Steps 2 and 3 are similar to a procedure call. But the interrupt is
asynchronous.

  4. As with a trap, the hardware automatically switches the system into supervisor mode. (It might have been in supervisor mode already. That is, an interrupt can occur in supervisor or user mode.)

#### Actions by the interrupt handler (et al) upon being activated

  5. An assembly language routine saves registers.
  6. The assembly routine sets up a new stack. (These last two steps are often called setting up the C environment.)
  7. The assembly routine calls a procedure in a high level language, often the C language (Tanenabaum forgot this step).
  8. The C procedure does the real work. 
    * Determines what caused the interrupt (in this case a disk completed an I/O).
    * How does it figure out the cause? 
      * It might know the priority of the interrupt being activated.
      * The controller might write information in memory before the interrupt.
      * The OS might read registers in the controller.
    * Mark process Q as ready to run. 
      * That is move Q to the _ready list_ (note that again we are viewing Q as a data structure).
      * Q is now in the ready state; it was in the blocked state before.
      * The code that Q needs to run initially is likely to be OS code. For example, the data just read is probably now in kernel space and the OS needs to copy it into user space.
    * Now we have at least two processes ready to run, namely P and Q. There may be arbitrarily many others.
  9. The scheduler decides which process to run, P or Q or something else. (This very loosely corresponds to g calling other procedures in the simple f calls g case we discussed previously). Eventually the scheduler decides to run P.

#### Actions by The OS When Returning Control to P

  10. The C procedure (that did the real work in the interrupt processing) continues and returns to the assembly code.
  11. Assembly language restores P's state (e.g., registers) and starts P at the point it was when the interrupt occurred.

#### Properties of Interrupts

  * Phew.
  * Unpredictable (to an extent). We cannot tell what was executed just _before_ the interrupt occurred. That is, the control transfer is asynchronous; it is difficult to ensure that everything is always prepared for the transfer.
  * The user code is _unaware_ of the difficulty and cannot (easily) detect that it occurred. This is another example of the OS presenting the user with a virtual machine environment that is more pleasant than reality (in this case synchronous rather asynchronous behavior).
  * Interrupts can also occur when the OS itself is executing. This can cause _serious_ difficulties since both the main line code (i.e., the code that was interrupted and the interrupt handling code are from the same program, namely the OS, and hence might well be using the same variables. We will soon see how this can cause great problems even in what appear to be trivial cases.
  * The interprocess control transfer is _neither_ stack-like _nor_ queue-like:  
If P was running, then Q was running, then R was running, then S was running,
and finally the interrupt occurs, the next process to be run might be any of
P, Q, R, or S (or some other process).

  * The system might have been in user-mode or supervisor mode when the interrupt occurred. The interrupt processing starts in supervisor mode.

#### The OS Running As a User Process

In traditional Unix and Linux, if an interrupt occurs while a user process
with PID=_P_ is running, the system switches to kernel mode and OS code is
executed, but the PID is still _P_. The owner of process _P_ is charged for
this execution. Try running the time program on one of the Unix systems and
noting the output.

### 2.1.7 Modeling Multiprogramming (Crudely)

Consider a job that is unable to compute (i.e., it is waiting for I/O) a
fraction p of the time.

  * With monoprogramming, the CPU utilization is 1-p.
  * Note that p is often > .5, so CPU utilization is poor.
  * But, if n jobs are in memory, then the probability that all n are waiting for I/O is approximately pn. So, with a **multiprogramming level** (MPL) of n, the CPU utilization is approximately 1-pn.
  * If p=.5 and n=4, then the utilization 1-pn=15/16 is much better than the monoprogramming (n=1) utilization of 1/2.

There are at least two causes of inaccuracy in the above modeling procedure.

  * Some CPU time is spent by the OS in switching from one process to another. So the "useful utilization", i.e. the proportion of time the CPU is executing user code, is lower than predicted.
  * The model assumes that the probability that one process is waiting for I/O is independent of the probability that another process is waiting for I/O. This assumption was used when we asserted that the probability all n jobs are waiting for I/O is pn.

Nonetheless, it is correct that increasing MPL does increase CPU utilization
up to a point.

An important limitation is memory. That is, we assumed that we have many jobs
loaded at once, which means we must have enough memory for them. There are
other memory-related issues as well and we will discuss them later in the
course.

**Homework:**

  * 1\. In Figure 2-2, three process states are shown. In theory, with three states, there could be six transitions. However, only four transitions are shown. Are there any circumstances in which either of both of the missing transitions might occur?
  * What is the key difference between a trap and an interrupt?
  * 7\. Multiple jobs can run in parallel and finish faster than if they had run sequentially. Suppose that two jobs, each of which needs 10 minutes of CPU time, start simultaneously. How long with the last one take to complete if they run sequentially? How log if they run in parallel? Assume 50% I/O wait.

**Remark**: Our final exam is Thursday 12 May at 4PM. Check out [ the official list](//cs.nyu.edu/dynamic/courses/exams)

![threads](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/threads.png)

## 2.2 Threads

The idea behind _threads_ to have separate threads of control (hence the name)
running in the address space of a single process as shown in the diagram to
the right. An _address space_ is a memory management concept. For now think of
an address space as the memory in which a process runs. (In reality it also
includes the mapping from virtual addresses, i.e., addresses in the program,
to physical addresses, i.e., addresses in the machine).

Each thread is somewhat like a process (e.g., it shares the processor with
other threads), but a thread contains less state than a process (e.g., the
address space belongs to the process in which the thread runs.)

### 2.2.1 Thread Usage

Often, when a process P executing an application is blocked (say for I/O),
there is still computation that can be done for the application. Another
process can't do this computation since it doesn't have access to P's memory.
But two threads in the same process do share memory so that problem doesn't
occur.

The downside of this memory sharing among threads is that each thread is not
protected from the others in its process. We will see in section 2.3 that
having multiple threads concurrently accessing the same memory can cause
subtle bugs is programs that look too simple to be wrong.

So it is a ofter performance/simplicity trade-off.

#### Two Threads in One Process vs Two Processes

Although there are many differences, we will be primarily interested in just
two.

  1. Threads in the same process share memory.
  2. Switching execution from one thread to another in the same process is much faster than switching execution from one process to another processes.

#### A Producer Consumer Pipeline

    
    
    loop
      Read 10KB from disk1 to inBuffer
      Compute from inBuffer to outBuffer
      Write outBuffer to disk2
    end loop
     
     
     
    //  process 1
    loop
      Read data from disk1 to inBuffer
    end loop
     
    //  process 2
    loop
      Compute from inBuffer to outBuffer
    end loop
     
    //  process 3
    loop
      Write outBuffer to disk2
    end loop
    

Consider the first frame of code on the right. Assume for simplicity each line
takes 10ms so the entire loop processes 10KB every 30ms. However, the CPU is
busy only during the second line and, (if the I/O system is sophisticated),
the first and third lines use separate hardware.

Hence in principle the three lines could all proceed at the same time. That is
we could turn the three steps into a pipeline so that after the startup phase,
the loop would process 10KB every 10ms, a 3X speed improvement.

The second frame show an attempt to speed up the application by splitting it
into three processes: a reader, a computer, and a writer. However this can't
work since the two inBuffers are not the same so processes 1 and 2 aren't
communicating. Similarly for processes 2 and 3.

If instead the three loops were each a thread within the same process, then
the two uses of inBuffer would refer to the same variable and similarly for
outBuffer. Hence our desired speedup would occur.

Another advantage of the threaded solution over the separate process non-
solution, is that the system can switch between threads in the same process
faster than it can switch between separate processes.

##### Double Buffering in the Producer Consumer Pipeline

The solution above is simplistic and would fail. Users of the same buffer must
coordinate their actions, and you need at least two inBuffers and two
outBuffers as shown in the solution immediately following.

The diagram on the right shows the actions during the first four time stems.
The disk on the right contains the input and the one on the left will contain
the output. The two circles on the right are input buffers and the two on the
left are output buffers. Initially, all the buffers are invalid (i.e., contain
no data).

![pipeline](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/pipeline.png)

  1. During the first time step, as indicated by the arrow in the diagram, thread 1 reads data from the input disk to the top input buffer. For this time step one disk is active (thread 1), the other disk (thread 3) and the cpu (thread 2) are inactive, which is no better that the simpler non-threaded solution.  
  

  2. The second time step is better. Thread 1 again reads data from the input disk, but this time into the bottom input buffer. The top input buffer is blue indicating that it contains valid data. Thread 2 uses the cpu to compute during this time step. It reads from the top input buffer and writes to the top output buffer. Note that the thread is reading valid data. Both thread 1 and thread 2 are active during this time step.   
  

  3. Starting with the third time step, we hit top speed, all three threads are busy. Thread 1 reads the input disk into the top input buffer, overwriting what was written before (that is why the circle is no longer blue). Thread 2 computes using the bottom buffers. Thread 3 writes from the top (blue, i.e. valid) output buffer to the output disk.  
  

  4. Subsequent time step are similar to time step 3 (until the input is exhausted). As shown in the diagram, these steps alternate their usage of the top and bottom buffers.

#### A Multithreaded Web Server

An important modern example of threading is a multithreaded web server. Each
thread is responding to a single WWW connection. While one thread is blocked
on I/O, additional threads can process other WWW connections.  
**Question**: Why not use separate processes, i.e., what is the shared memory?  
**Answer**: The cache of frequently referenced pages.

#### Dispatchers and Workers

A common organization for a multithreaded application is to have a dispatcher
thread that fields requests and then passes each request on to an idle worker
thread. Since the dispatcher and workers share memory, passing the request is
very low overhead.

A multithreaded web server can be organized this way.

#### Helper Tasks

A final (related) example occurs when a main line task interfaces with the
user and sometimes needs to perform a lengthy task that does not directly
affect the user-interface.

Tanenbaum considers a word processor currently editing a large file (say a
book the user is writing) and the user deletes a word early in the book. This
can cause changes on all subsequent pages. Hence, reformatting the book could
cause a detectable delay in the user interface. With a threaded
implementation, a second thread can be assigned the reformatting task while
the primary thread continues to interface with the user. It is only when the
user wishes to examine a page near the end of the book that they must wait for
the second thread to finish. Hopefully, the user has been doing other editing
in the beginning of the book so that the second thread is finished prior to
the user needing to access pages near the end. Even if the second thread is
not finished, it will have accomplished some of the work while the user is
still editing near the book's beginning.

In this same example, the word processor may wish to perform automatic
backups. Again another thread to do this. In this way the thread that
interfaces with the user is not blocked during the backup. However some
coordination between threads may be needed so that the backup is of a
consistent state.

### 2.2.2 The Classical Thread Model

Process-Wide vs Thread-Specific Items

Per process itemsPer thread items

Address space

Program counter

Global variables

Machine registers

Open files

Stack

Child processes

Pending alarms

Signals and signal handlers

Accounting information

A process contains a number of resources such as address space, open files,
accounting information, etc. In addition to these resources, a process has a
thread of control, e.g., program counter, register contents, stack. The idea
of threads is to permit multiple threads of control to execute within one
process. This is often called **multithreading** and threads are sometimes
called **lightweight processes**. Because threads in the same process share so
much state, switching between them is much less expensive than switching
between separate processes. The table on the right shows which properties are
common to all threads in a given process and which properties are thread
specific.

Individual threads within the same process are not completely independent. For
example there is no memory protection between them. This is typically not a
security problem as the threads are cooperating and all are from the same user
(indeed the same process). However, the shared resources do make debugging
harder. For example one thread can easily overwrite data needed by another
thread in the process and when the second thread fails, the cause may be hard
to determine because the tendency is to assume that the failed thread caused
the failure.

You may recall that a serious advantage of microkernel OS design was that the
separate OS processes could not, even if buggy, damage each others data
structures.

A new thread in the same process is created by a routine named something like
_thread_create_; similarly there is _thread_exit_. The analogue to waitpid is
_thread_join_ (the name presumably comes from the fork-join model of parallel
execution).

The routine _tread_yield_, which relinquishes the processor, does not have a
direct analogue for processes. The corresponding system call (if it existed)
would move the process from running to ready. It would be as if the process
preempted itself.

**Homework:** 15\. Why would a thread ever voluntarily give up the CPU by calling thread_yield? After all, since there is no periodic clock interrupt, it may never get back the CPU?

#### Challenges and Questions

Assume a process has several threads. What should we do if one of these
threads

  1. Executes a fork?
  2. Closes a file?
  3. Requests more memory?
  4. Moves a file pointer via lseek?

### 2.2.3 POSIX Threads

POSIX threads (pthreads) is an IEEE standard specification that is supported
by many Unix and Unix-like systems. Pthreads follows the classical thread
model above and specifies routines such as pthread_create, pthread_yield, etc.

An alternative to the classical model are the so-called Linux threads, which
are discussed in section 10.3 of the 4e.

### 2.2.4 Implementing Threads in User Space

Write a (threads) library that acts as a mini-scheduler and implements
_thread_create_, _thread_exit_, _thread_wait_, _thread_yield_, etc. This
library acts as a run-time system for the threads in this process. The central
data structure maintained and used by this library is a _thread table_, the
analogue of the process table in the operating system itself.

There is a thread table and an instance of the threads library in _each_
multithreaded process.

Advantages of User-Mode Threads:

  * Requires **no** OS modification. Previously, this was the primary advantage since most operating systems did not support threads. Now, the major systems do support threads so this advantage is less significant. 
  * Very fast since no context switching.
  * Can customize the scheduler for each application.

Disadvantages

  * Blocking system calls cannot be executed directly since that would block the entire process. For example, consider the producer consumer example above implemented in the natural manner with user-mode threads. This implementation would not work well since, whenever an I/O was issued that caused the process to block, all the threads would be unable to run (but see just below).
  * Similarly a page fault would block the entire process (i.e., all the threads).
  * In addition, a thread with an infinite loop prevents all other threads in this process from ever running.

#### Possible Methods of Dealing With Blocking System Calls

  * Perhaps the OS supplies a non-blocking version of the system call, e.g. a non-blocking read.
  * Perhaps the OS supplies another system call that tells if the blocking system call will in fact block. For example, a unix select() can be used to tell if a read would block. It might not block if, for example, 
    * The requested disk block is in the buffer cache (see the I/O chapter).
    * The request was for a keyboard or mouse or network event that has already happened.

#### Relevance to Multiprocessors/Multicore

For a uniprocessor, which is all we are officially considering, there is
little gain in splitting pure computation into pieces. If the CPU is to be
active all the time for all the threads, it is simpler to just have one
(unithreaded) process.

But this changes for multiprocessors/multicores. Now it is **very** useful to
split computation into threads and have each executing on a separate
processor/core. In this case, user-mode threads are wonderful, there are no
system calls and the extremely low overhead is beneficial.

However, there are serious issues involved is programming applications for
this environment.

### 2.2.5 Implementing Threads in the Kernel

Modern operating systems have direct support for threads, i.e., the thread
operations are implemented in the kernel itself. This naturally required that
the operating system was (significantly) modified and was not a trivial
undertaking.

  * There is only one thread table for the entire system and it is in the OS.
  * Thread-create and friends are now system calls and hence much slower than with user-mode threads. They are, however, still much faster than creating/switching/etc processes since there is so much shared state that does not need to be recreated.
  * A thread that blocks causes no particular problem. The kernel can run another thread from this process (or can run a thread from another process).
  * Similarly a page fault or infinite loop in one thread does not automatically block the other threads in the process.

### 2.2.6 Hybrid Implementations

One can write a (user-level) thread library even if the kernel also has
threads. This is sometimes called the N:M model since N user-mode threads run
on M kernel threads. In this scheme, the kernel threads cooperate to execute
the user-level threads.

  * Different kernel threads in the same process can have differing numbers of user threads assigned to them.
  * Switching between user-level threads within one kernel thread is very fast (no context switch). It is essentially the same as in the case of pure user-mode threads.
  * Switching between kernel threads of the same process requires a system call and is essentially the same as in the case of pure kernel-level threads.
  * Since a blocking system call or page fault blocks only one kernel thread, the multi-threaded application as a whole can still run since user-level threads in other kernel-level threads of this process are still runnable.

An offshoot of the N:M terminology is that kernel-level threading (without
user-level threading) is sometimes referred to as the 1:1 model since one can
think of each thread as being a user level thread executed by a dedicated
kernel-level thread.

**Homework:**.

  * 16\. Can a thread ever be preempted by a clock interrupt. If so, under what circumstances? If not, why not?
  * 18\. What is the biggest advantage of implementing threads in user space? What is the biggest disadvantage?

### 2.2.7 Scheduler Activations

Skipped

### 2.2.8 Popup Threads

The idea is to automatically issue a thread-create system call upon message
arrival. (The alternative is to have a thread or process blocked on a
_receive_ system call.) If implemented well, the latency between message
arrival and thread execution can be very small since the new thread does not
have state to restore.

### 2.2.9 Making Single-threaded Code Multithreaded

Definitely _NOT_ for the faint of heart.

  * There often is state that should not be shared. A well-cited example is the unix _errno_ variable that contains the error number (zero means no error) of the error encountered by the last system call. Errno is hardly elegant (even in normal, single-threaded, applications), but its use is widespread. If multiple threads issue faulty system calls the errno value of the second overwrites the first and thus the first errno value may be lost.
  * Much existing code, including many libraries, are not _re-entrant_.
  * Managing the shared memory inherent in multi-threaded applications opens up the possibility of race conditions that we will be studying next.
  * What should be done with a signal sent to a process. Does it go to all or one thread?
  * How should stack growth be managed. Normally the kernel grows the (single) stack automatically when needed. What if there are multiple stacks?

**Note**: We shall do section 2.4 before section 2.3 for two reasons.

  1. Sections 2.3 and 2.5 are closely related; having 2.4 in between seems awkward to me.
  2. Lab 2 will use material from 2.4 so I don't want to push 2.4 after 2.5.

![process-states](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/process-
states.png)

## 2.4 Process Scheduling

Scheduling processes on the processor is often called processor scheduling or
process scheduling or simply scheduling. As we shall see later in the course,
a more precise name would be short-term, processor scheduling.

At this point we are discussing the two arcs connecting running↔ready in the
diagram on the right, which shows the various states of a process and the
transitions between those states. Medium term scheduling is discussed later
(as is disk-arm scheduling).

As you would expect, the part of the OS responsible for (short-term,
processor) scheduling is called the (short-term, processor) **scheduler** and
the algorithm used is called the (short-term, processor) **scheduling
algorithm**.

### 2.4.1 Introduction to Scheduling

#### Importance of Scheduling for Various Generations and Circumstances

Early computer systems were monoprogrammed and, as a result, scheduling was a
non-issue.

For many current personal computers, which are definitely multiprogrammed,
there is in fact very rarely more than one runnable process. As a result,
scheduling is not critical.

For servers, scheduling is indeed important and these are the systems you
should think of.

#### Process Behavior

A processes alternates between CPU activity and I/O activity, which I often
refer to as CPU bursts and I/O bursts. In particular the Scheduling lab will
use that terminology.

Since (as we shall see when we study I/O) the time required for a disk access
depends only weakly on the size of the request, the key distinguishing factor
between compute-bound (aka CPU-bound) and I/O-bound jobs is the length of the
CPU bursts.

The trend over the past decade or two has been for more and more jobs to
become I/O-bound since the CPU speed has increased much faster than I/O speed.

Start Lecture #6

#### When to Schedule

An obvious point, which is often forgotten (I don't think 4e mentions it) is
that the scheduler **cannot** run unless the OS is running. In particular, for
the uniprocessor systems we are considering, no scheduling can occur when a
user process is running. (In the mulitprocessor situation, no scheduling can
occur when all processors are running user jobs).

We refer to the arcs in the state transition diagram above (especially the top
triangle) and discuss those transitions where scheduling is desirable and
those where it is manditory.

  1. Process creation.  
The running process has issued a fork() system call and hence the OS runs;
thus scheduling is **possible**. Scheduling is also **desirable** at this time
since the scheduling algorithm might favor the new process.

  2. Process termination.  
The exit() system call has again transferred control to the OS so scheduling
is possible. Moreover, scheduling is **necessary** since the previously
running process has terminated.

  3. Process blocks.  
Same as termination.

  4. Process is unblocked (note grammatical difference).  
This was most likely due to I/O interrupt being received. Since the OS takes
control, scheduling is possible. When an I/O interrupt occurs, this normally
means that a blocked process is now ready. Hence, we have a new runnable
process and scheduling is therefore **desirable**.

  5. Process is preempted.  
Preemption requires a clock interrupt, at which point the OS is running so
scheduling is **possible**. Indeed, when the currently running process is
preempted, scheduling is **necessary**.

#### Preemption

It is important to distinguish preemptive from non-preemptive scheduling
algorithms.

  * A preemptive scheduler means the operating system can move a process from running to ready without the process requesting it.
  * Without preemption, the system implements run until completion, or block (or yield, if there is threading.
  * The preempt arc in the diagram is present for preemptive scheduling algorithms.
  * We do not emphasize yield (a solid arrow from running to ready).
  * Preemption needs a clock interrupt (or equivalent).
  * Preemption is needed to guarantee fairness.
  * Preemption is found in all modern general purpose operating systems.
  * Even non-preemptive systems can be multiprogrammed (remember that processes do block for I/O).
  * Preemption is expensive.

#### Categories of Scheduling Algorithms

We distinguish three categories of scheduling algorithms with regard to the
importance of preemption.

  1. Batch.
  2. Interactive.
  3. Real Time.

For multiprogramed batch systems (we do not consider uniprogrammed systems,
which have no need for schedulers) the primary concern is efficiency. Since no
user is waiting at a terminal, preemption is not crucial and if it is used, it
is performed rarely, i.e., each process is given a long time period before
being preempted.

For interactive systems (and multiuser servers), preemption is crucial for
fairness and rapid response time to short requests.

We don't study real time systems in this course, but will say that preemption
is typically not important since all the processes are cooperating and are
programmed to do their task in a prescribed time window.

#### Scheduling Algorithm Goals

There are numerous objectives, several of which conflict, that a scheduler
tries to achieve. These include.

  1. Fairness.  
Treating users uniformly, which must be balanced against ...

  2. Respecting priority.  
That is, favoring jobs considered more important. For example, if my laptop is
trying to fold proteins in the background, I don't want that activity to
appreciably slow down my compiles and especially don't want it to make my
system seem sluggish when I am modifying these class notes. In general,
interactive jobs should have higher priority.

  3. Efficiency.  
This has two aspects.

    * Do not spend excessive time in the scheduler.
    * Try to keep all parts of the system busy.
  4. Low turnaround time  
That is, minimize the time from the submission of a job to its termination.
This is important for batch jobs.

  5. High throughput.  
That is, maximize the number of jobs completed per day. Not quite the same as
minimizing the (average) turnaround time as we shall see when we discuss
shortest job first.

  6. Low response time.  
That is, minimize the time from when an interactive user issues a command to
when the response is given. This is very important for interactive jobs.  
Again, as we shall soon see when studying shortest job first, minimizing
response time, is not the same as maximizing throughput.

  7. Repeatability.  
Dartmouth (DTSS) wasted cycles and limited logins for repeatability.

  8. Degrade gracefully under load.

#### Deadline scheduling

This is used for real time systems. The objective of the scheduler is to find
a schedule for all the tasks (there are a fixed set of tasks) so that each
meets its deadline. The run time of each task is known in advance.

Actually it is more complicated.

  * Periodic tasks.
  * What if we can't schedule all task so that each meets its deadline (i.e., what should be the penalty function)?
  * What if the run-time is not constant but has a known probability distribution?

#### The Name Game

There is an amazing inconsistency in naming the different (short-term,
processor) scheduling algorithms. Over the years I have used primarily 4
books: In chronological order they are Finkel, Deitel, Silberschatz, and
Tanenbaum. The table just below illustrates the name game for these four
books. After the table we discuss several scheduling policy in some detail.

    
    
      Finkel  Deitel  Silbershatz Tanenbaum
      -------------------------------------
      FCFS    FIFO    FCFS        FCFS
      RR      RR      RR          RR
      PS      **      PS          PS
      SRR     **      SRR         not in tanenbaum
      SPN     SJF     SJF         SJF/SPN
      PSPN    SRT     PSJF/SRTF   SRTN
      HPRN    HRN     **          not in tanenbaum
      **      **      MLQ         only in silbershatz
      FB      MLFQ    MLFQ        MQ
    

**Note**: For an alternate organization of the scheduling algorithms (due to my former PhD student Eric Freudenthal and presented by him Fall 2002) click [here.](scheduling-eric.pdf)

### 2.4.2 Scheduling in Batch Systems

#### First Come First Served (FCFS, FIFO, FCFS, FCFS)

If the OS doesn't schedule, it still needs to store the list of ready
processes in some manner. If it is a queue you get FCFS. If it is a stack, you
get LCFS. Perhaps you could get some sort of random policy as well.

  * Only FCFS is ever used in practice.
  * **Non-**preemptive.
  * The simplist scheduling policy.
  * In some sense the fairest since it is first come first served. But perhaps that is not so fair. Consider a 1 hour job submitted one second before a 3 second job.
  * An efficient usage of cpu in the sense that the scheduler is very fast.
  * Does not favor interactive jobs.

#### Shortest Job First (SPN, SJF, SJF, SJF)

Sort jobs by execution time needed and run the shortest first.

This is a **Non**-preemptive algorithm.

First consider a static (overly simple, non-realistic) situation where all
jobs are available in the beginning and we know how long each one will take to
run. For simplicity lets consider run-to-completion, also called uniprogrammed
(i.e., we don't even switch to another process on I/O).

In this situation, uniprogrammed SJF has the shortest average waiting time.
Here's why.

  * Assume you have a schedule with a long job right before a short job.
  * Consider swapping these two jobs.
  * This swap decreases the wait for the short job by the length of the long job and increases the wait of the long job by the length of the short job.
  * Since the gain for the short job exceeds the loss for the long job, the swap decreases the total waiting time for these two.
  * It does not affect any other job's wait.
  * Hence the swap decreases the total waiting for all jobs and hence decreases the average waiting time as well.
  * In summary, whenever a long job is right before a short job, we can swap them and decrease the average waiting time.
  * Thus the lowest average turnaround time occurs when there are no short jobs right before long jobs, i.e., the shortest jobs are first (SJF). Indeed, we have shorted the jobs in order of increasing run times.

The above argument illustrates an advantage of favoring short jobs: the
average waiting time is reduced. For example we will soon learn about RR. An
argument for making the RR quantum is small is that short jobs are favored

In the more realistic case of true SJF where the scheduler switches to a new
process when the currently running process blocks (say for I/O), I would call
the policy shortest next-CPU-burst first. However, I have never heard anyone
(except me) call it that.

The real difficulty is predicting the future (i.e., knowing in advance the
time required for the job or the job's next-CPU-burst).

One way to estimate the duration of the next CPU burst is to calculate a
weighted average of the duration of recent CPU bursts. Tanenbaum calls this
Shortest Process Next.

Shortest Job First can starve a process that requires a long burst.

Starvation can be prevented by the standard technique.  
**Question**: What is that technique?  
**Answer**: Priority aging (see below).

#### Shortest Remaining Time Next (PSPN, SRT, PSJF/SRTF, SRTN)

Preemptive version of above. Indeed some authors call it preemptive shortest
job first.

Permit a process that enters the ready list to preempt the running process if
the time for the new process (or for its next burst) is less than the
_remaining_ time for the running process (or for its current burst).

It will never happen that a process already in the ready list will require
less time than the remaining time for the currently running process.  
**Question**: Why?  
**Answer**: When the process joined the ready list it would have started running if the current process had more time remaining. Since that didn't happen the currently running job then had less time remaining and now it has even less.

SRTN Can starve a process that requires a long burst.

Starvation can be prevented by the standard technique.  
**Question**: What is that technique?  
**Answer**: Priority aging (see below).

Start Lecture #7

### 2.4.3 Scheduling in Interactive Systems

The following algorithms can also be used for batch systems, but in that case,
the gain may not justify the extra complexity.

#### Round Robin (RR, RR, RR, RR)

Round Robin (RR) is an important _preemptive _ policy. It is essentially the
preemptive version of FCFS. One property of RR is that it loosely approximates
SJF without knowing in advance how long each process will require.

When a process is put into the running state a timer is set to q milliseconds,
a key parameter of the policy, called the _quantum_. If the timer goes off and
the process is still running, the OS **preempts** the process.

  * Preemption requires a clock interrupt so that OS can take control when the quantum expires.
  * The currently running process is moved to the ready state (the _preempt_ arc in my favorite diagram), where it is placed at the rear of the ready list.
  * The process at the front of the ready list is removed from the list and run (i.e., moves to state running).

Note that, as in FCFS, the ready list is being treated as a queue. Indeed many
always call the list of ready processes the ready queue. But I don't. For
other scheduling algorithms the ready list is not accessed in a FIFO manner so
I find the term queue misleading. For FCFS and RR, the term ready queue is
appropriate.

When a process is created or unblocked, it is likewise placed at the rear of
the ready list.

Note that RR with a quantum of say 10ms. works well if you have a 1 hr job and
then a 1 second job. This is the sense in which it approximates SJF.

As q gets large, RR approaches FCFS. Indeed if q is larger that the longest
time any process will run before terminating or blocking, then RR **is** FCFS.
A good way to see this is to look at my favorite diagram and note the three
arcs leaving running. They are triggered by three conditions: process
terminating, process blocking, and process preempted. If the first trigger
condition to arise is never preemption, we can erase that arc and then RR
becomes FCFS.

As q gets small, RR approaches PS (Processor Sharing, described next).

**Question:** What value of q should we choose?  
**Answer:** A trade-off exists.

  * A small q makes the system more responsive, a long compute-bound job cannot delay a short job for an excessive period.
  * A large q makes the system more efficient since there is less process switching.
  * A reasonable time for q is a few tens of milliseconds or perhaps a few milliseconds for a very fast system. (millisecond = 1/1000 second and is abbreviated ms). This means every other job can delay your job receiving some attention by at most q (plus the context switch time CS, which is much less than 1ms). Also the overhead is CS/(CS+q), which is small.

A student  found the following reference for the name Round Robin in the
Encyclopedia of Word and Phrase Origins by Robert Hendrickson (Facts on File,
New York, 1997). A similar, but less detailed, citation can be found in
wikipedia.

> The round robin was originally a petition, its signatures arranged in a
circular form to disguise the order of signing. Most probably it takes its
name from the ruban rond, (round ribbon), in 17th-century France, where
government officials devised a method of signing their petitions of grievances
on ribbons that were attached to the documents in a circular form. In that way
no signer could be accused of signing the document first and risk having his
head chopped off for instigating trouble. Ruban rond later became round robin
in English and the custom continued in the British navy, where petitions of
grievances were signed as if the signatures were spokes of a wheel radiating
from its hub. Today round robin usually means a sports tournament where all of
the contestants play each other at least once and losing a match doesn't
result in immediate elimination.

**Homework:** Round-robin schedulers normally maintain a list of all ready processes, with each process occurring exactly once in the list. What would happen if a process occurred more than once in the list? Can you think of any reason for allowing this?

**Homework:** Give an argument favoring a large quantum; give an argument favoring a small quantum.

ProcessCPU TimeCreation Time

P1

20

0

P2

3

3

P3

2

5

**Homework:**

  * Consider the set of processes in the table to the right.
  * Assume each process performs no I/O, i.e., no process ever blocks.
  * When does each process finish if RR scheduling is used with q=1, if q=2, if q=3, if q=100?
  * First assume (unrealistically) that context switch time is zero.
  * Then assume it is 0.1.
  * All times are in milliseconds.
  * The CPU time is the total time required for the process (excluding any context switch time).
  * The creation time is the time when the process is created. So P1 is created when the problem begins and P3 is created 5 milliseconds later.
  * If two processes have equal priority (in RR this means if they both enter the ready state at the same cycle), we give priority (in RR this means place first on the queue) to the process with the earliest creation time. If they also have the same creation time, then we give priority to the process with the lower number, i.e., P1 has priority over P2, which in turn has priority over P3. Since I plan on using this rule for lab 2, I will refer to it as the lab 2 tie-breaking rule.
  * Remind me to discuss this problem in class next time.

**Homework:** Redo the previous homework for q=2 with the following changes. After process P1 runs for 3ms (milliseconds), it blocks for 2ms. P1 never blocks again. That is, P1 begins with a CPU burst of 3ms, then has an I/O burst of 2ms, and finally it has a CPU burst of 20-3 = 17ms. P2 never blocks. After P3 runs for 1 ms it blocks for 1ms. Assume the context switch time is zero. Remind me to answer this problem in class next lecture.

#### Processor Sharing (PS, **, PS, PS)

Merge the ready and running states and permit all ready jobs to be run at
once. However, the processor slows down so that when n jobs are running at
once, each progresses at a speed 1/n as fast as it would if it were running
alone.

  * Clearly impossible as stated due to the overhead of process switching.
  * Of theoretical interest (easy to analyze).
  * Approximated by RR with a small quantum. Make **sure** you understand this last point. For example, consider the last homework assignment (with zero context switch time and no blocking) and consider q=1, q=.1, q=.01, etc.
  * Show what happens with PS for 3 processes, A, B, C, each requiring 3 seconds of CPU time. A starts at time 0, B at 1 second, C at 2.
  * Consider three processes all starting at time 0. One requires 1ms, the second 100ms, the third 10sec (seconds). Compute the total/average waiting time for RR q=1ms, PS, SJF, SRTN, and FCFS. Note that this depends on the order the processes happen to be processed in. The effect is huge for FCFS, modest for RR with modest quantum, and non-existent for PS and SRTN.

**Homework:** 38.

#### Variants of Round Robin

  1. _State dependent RR_
    * Same as RR but q is varied dynamically depending on the state of the system.
    * Favor processes holding important resources, for example, non-swappable memory.
    * Perhaps this should be considered medium term scheduling since you probably do not recalculate q each time.
  2. _External priorities_: RR but a user can pay more and get bigger q. That is, one process can be given a higher priority than another. But this is not an absolute priority: the lower priority (i.e., less important) process does get to run, but not as much as the higher priority process.

#### Priority Scheduling

Each job is assigned a priority (externally, perhaps by charging more for
higher priority) and the highest priority ready job is run.

  * Sometimes a large priority means an important job; sometimes a small priority means an important job.
  * Similar to External priorities above.
  * If many processes have the highest priority, use RR among them. Indeed one often groups several priorities into a priority class and employs RR within a class.
  * Can easily starve processes, which can be fixed by the standard technique, which is right below.
  * Can have the priorities changed dynamically to favor processes holding important resources  (similar to state dependent RR above).
  * Many policies can be thought of as priority scheduling in which we run the job with the highest priority. The different scheduling policies have different notions of priority. For example: 
    * FCFS and RR are priority scheduling where the priority is the time last inserted on the ready list.
    * SJF and SRTN are priority scheduling, where the priority of the job is the time it needs to run in order to complete (or complete its current CPU burst).

#### Two Examples to Do in Class

  1. FCFS with three processes, A, B, and C. Each CPU burst is 3 time units (ms if you like). Each I/O burst is also 3. Show the ready queue.
  2. Then repeat for RR with q=2.

####  Priority Aging--The Standard Technique to Prevent Starvation

As a job is waiting, increase its priority; hence it will eventually have the
highest priority.

  * **Starvation** means that from a certain time on, some process never runs, because it never has the highest priority. The formal way to say this is that a system is free of starvation if, No job can remain in the ready state forever.
  * Priority aging is the standard technique used to prevent starvation (assuming all jobs terminate or the policy is preemptive).
  * There may be many processes with the maximum priority.
  * If so, can schedule those with max priority using FIFO (risks starvation if a job doesn't terminate) or RR (the preemptive equivalent).
  * We can apply priority aging to many policies, in particular to priority scheduling described above.

**Homework:** 44, 45. Note that when the book says RR with each process getting its fair share, it means Processor Sharing.

![srr.png](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/srr.png)

#### Selfish RR (SRR, **, SRR, **)

SRR is a preemptive policy in which unblocked (i.e. ready and running)
processes are divided into two classes the Accepted processes, which are
scheduled using RR and the others, which are not run until they become
accepted. (Perhaps SRR really stands for snobbish RR).

  * A new process starts at priority 0.
  * Accepted process have their priority increase at rate a≥0.
  * A non-accepted process has its priority increases at rate b≥0.
  * A non-accepted process becomes accepted when its priority reaches that of the accepted processes (or when there are no accepted processes and it has the highest priority of the unaccepted processes).
  * Hence, once a process is accepted, it remains accepted until it terminates (or blocks, see below). Also all accepted processes have same priority.
  * Note that, when the only accepted process terminates (or blocks, see below), all the process with the next highest priority become accepted.
![srr-2](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/srr-2.png)

The behavior of SRR depends on the relationships between a, b, and zero. There
are four cases.

  * If a=0, get RR.
  * If a≥b>0, get FCFS.
  * If b>a>0, it is interesting.
  * If a>b=0, you get RR in batches. This is similar to n-step scan for disk I/O.

It is not clear what to do to the priority when a process blocks. There are
several possibilities.

  1. Reset the priority to zero when a process is blocked. In this case unblock acts like create in terms of priority.
  2. Freeze the priority at its current value. When it unblocks, the process will have the same priority it had when it was blocked.
  3. Let the priority continue to grow as if the process was not blocked. The growth can be a rate a or b depending on whether the process was accepted at the time of blockage. Presumably a process can become accepted during blockage if the other currently accepted processes terminate.

The third possibility seems a little weird. We shall adopt the first
possibility (reset to zero) since it seems the simplest.

#### Approximating the Behavior of SFJ and PSJF

Recall that SFJ/PSFJ do a good job of minimizing the average waiting time. The
problem with them is the difficulty in finding the job whose next CPU burst is
minimal. We now learn three scheduling algorithms that attempt to do this. The
first algorithm does it statically, presumably with some manual help; the
other two are dynamic and fully automatic.

#### Multilevel Queues (**, **, MLQ, **)

Put different classes of processs in different queues

  * Processes do not move from one queue to another.
  * Can have different policies on the different queues.  
For example, might have a background (batch) queue that is FCFS and one or
more foreground queues that are RR (possibly with different quanta).

  * Must also have a policy _among_ the queues.  
For example, might have two queues, foreground and background, and give the
first absolute priority over the second

    * Might apply priority aging to prevent background starvation.
    * But might not, i.e., no guarantee of service for background processes.
    * Might have 3 queues, foreground, background, no-cost (and might starve).
  * Another possible **inter**-queue policy would be have 2 queues, apply RR to each but cycle through the higher priority queue twice and then cycle through the lower priority queue once.

#### Multiple Queues (FB, MFQ, MLFBQ, MQ)

As with multilevel queues above, we have many queues, but now processes move
from queue to queue in an attempt to dynamically separate batch-like from
interactive processs so that we can favor the latter.

Remember that low average waiting time is achieved by SJF. Multiple Queues is
an attempt to determine dynamically those processes that are interactive,
which means have very short cpu bursts.

  * Run processes from the highest priority nonempty queue in a RR manner.
  * When a process uses its full quanta (acts a like batch process), move it to a lower priority queue.
  * When a process doesn't use a full quanta (acts like an interactive process), move it to a higher priority queue.
  * A long process with frequent (perhaps spurious) I/O will remain in the better queues.
  * Might have the bottom queue FCFS.
  * Many variants.  
For example, might let process stay in top queue 1 quantum, next queue 2
quanta, next queue 4 quanta (i.e., sometimes return a process to the rear of
the same queue it was in if the quantum expires).  
Might move to a higher queue only if a keyboard interrupt occurred rather than
if the quantum failed to expire for any other reason (e.g., disk I/O).

#### Shortest Process Next

![spn](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/spn.png)

Shortest process next (mentioned previously) is an attempt to apply sjf to
interactive scheduling. What is needed is an estimate of how long the process
will run until it blocks again. One method is to choose some initial estimate
when the process starts and then, whenever the process blocks choose a new
estimate via  
`     NewEstimate = A*OldEstimate + (1-A)*LastBurst  
` where 0<A<1 and LastBurst is the actual time used during the burst that just
ended.

#### Highest Penalty Ratio Next (HPRN, HRN, **, **)

Run the process that has been hurt the most.

  * For each process, let r = T/t; where T is how long this process has been in system and t is the running time of the process to date.
  * For example, r=2.5 means the job has been running 1/2.5 = 40% of the time it has been in the system.
  * We call r the _penalty ratio_ and run the process having the highest r value.
  * We must worry about a process that just enters the system since t=0 and hence the ratio is undefined. Define t to be the max of 1 and the running time to date. Since now t is at least 1, the ratio is always defined.
  * HPRN is normally defined to be non-preemptive (i.e., the system only checks r when a burst ends).
  * There is an preemptive analogue. That analogue differs from HPRN as follows. 
    * When putting a process into the run state compute the time at which it will no longer have the highest ratio and set a timer.
    * When a process is moved into the ready state, compute its ratio and preempt if needed.
  * HRN stands for highest response ratio next and means the same thing.
  * This policy is yet another example of priority scheduling.

#### Guaranteed Scheduling

A variation on HPRN. The penalty ratio is a little different. It is nearly the
reciprocal of the above, namely  
   t / (T/n)  
where n is the multiprogramming level. So if n is constant, this ratio is a
constant times 1/r.

#### Lottery Scheduling

Each process gets a fixed number of tickets and at each scheduling event a
random ticket is drawn (**with** replacement) and the process holding that
ticket runs for the next interval (probably a RR-like quantum q).

On the average a process with P percent of the tickets will get P percent of
the CPU (assuming no blocking, i.e., full quanta).

#### Fair-Share Scheduling

If you treat processes fairly you may not be treating users fairly since users
with many processes will get more service than users with few processes. The
scheduler can group processes by user and only give one of a user's processes
a time slice before moving to another user.

For example, linux has cgroups for a related purpose. The scheduler first
schedules across cgroups so if a big job has many processes in the same
cgroup, it will not get more time than a small job with just one process.

Fancier methods have been implemented that give some fairness to groups of
users. Say one group paid 30% of the cost of the computer. That group would be
entitled to 30% of the cpu cycles providing it had at least one process
active. Furthermore a group earns some credit when it has no processes active.

#### Theoretical Issues

Considerable theory has been developed.

  * NP completeness results abound.
  * Much work in queuing theory to predict performance.
  * Not covered in this course.

Start Lecture #8

![process-states](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/process-
states.png)

#### Medium-Term Scheduling

In addition to the short-term scheduling we have discussed, we add _medium-
term scheduling_ in which decisions are made at a coarser time scale.

Recall my favorite diagram, shown again on the right. Medium term scheduling
determines the transitions from the top triangle to the bottom row. We suspend
(swap out) some process if memory is over-committed, dropping the (ready or
blocked) process down. We also need resume transitions to return a process to
the top triangle.

Criteria for choosing a victim to suspend include:

  * How long since previously suspended.
  * How much CPU time used recently.
  * How much memory does it use.
  * External priority (pay more, get swapped out less).

We will discuss medium term scheduling again when we study memory management
and understand what is meant by saying memory is over-committed.

#### Review Homework Assigned Last Time

ProcessCPU  
TimeStart  
Time Blocks  
after/for

P0

10

0

5

9

P1

11

4

4

6

P2

9

4

 never

Consider the following problem of the same genre as those in the homework. In
this example we have RR scheduling with q=3 and zero context switch time.

The system contains three processes. Their relevant characteristics are given
in the table on the right.

The diagram below presents a detailed solution. The numbers above the
horizontal lines give the CPU time remaining at the beginning and end of the
execution interval. The numbers below the horizontal lines give the length of
the execution interval. The red lines indicate a blocked process.

We see that P2 finishes at time 21, P0 at time 23, and P1 at time 30.

![rr-example](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/rr-
example.png)

#### Long Term Scheduling

This is sometimes called Job scheduling.

  1. The system decides when to start jobs, i.e., it does not necessarily start them when submitted.
  2. Used at many supercomputer sites.

A similar idea (but more drastic and not always so well coordinated) is to
force some users to log out, kill processes, and/or block logins if over-
committed.

  * CTSS (an early time sharing system at MIT) did this to insure decent interactive response time.
  * Unix does this if out of memory.
  * Only LEM jobs during the day (Grumman).

### 2.4.4 Scheduling in Real Time Systems

### 2.4.5 Policy versus Mechanism

### 2.4.6 Thread Scheduling

#### Lab 2 (Scheduling) Discussion

    
    
      // A general program
      // that alternates
      // computing with I/O
      //
      // Compute with no I/O
      // I/O with no computing
      // Compute with no I/O
      // I/O with no computing
      // ...
      // Compute with no I/O
      // I/O with no computing
    

On the right is the general form of many programs, compute, I/O, compute, I/O,
..., compute, I/O. In lab 2 we characterize a program of this type by a tuple
of four nonnegative integers (A, B, C, IO), only A can be zero.

A is the arrival (or start) time and C is the (total) CPU time. These two were
used in the problems I did on the board.

B the CPU-burst time and IO the I/O-burst time, generalize the blocks after
and blocks for in the previous example. They are used to calculate the times
for each of the compute and I/O sections of the program on the right.

Show the detailed output

  1. In FCFS see the affect of A, B, C, and IO.
  2. In RR see how the cpu burst is limited.
  3. Note the intital sorting to ease finding the tie breaking process.
  4. Illustrate the show random option.
  5. Comment on how to do it: (time-based) discrete-event simulation (DES). 
    1. DoBlockedProcesses()
    2. DoRunningProcesses()
    3. DoArrivingProcesses()
    4. DoReadyProcesses()
  6. For processor sharing need event-based DES.

## 2.3 Interprocess Communication (IPC) and Coordination/Synchronization

### 2.3.1 Race Conditions

A **race condition** occurs when

  1. Two processes A and B are each about to perform some (possibly different) action.
  2. The program does not determine which process goes first.
  3. The result if A goes first differs from the result if B goes first.

In other words, there is a race between A and B and the program result differs
depending on which one wins the race.

**Notes:**

  1. There can be more that 2 competing processes.
  2. The interesting case is when one ordering, which occurs most frequently, gives the expected result, and another, rarely occurring, ordering give an unexpected result.
  3. The example below exhibits this interesting case.

Imagine two processes both accessing x, which is initially 10.

    
    
      A1: LOAD  r1,x     B1: LOAD  r2,x
      A2: ADD   r1,1     B2: SUB   r2,1
      A3: STORE r1,x     B3: STORE r2,x
    

  * One process is to execute x := x+1.
  * The other is to execute x := x-1.
  * When both are finished x should be 10.
  * But x := x+1 is not atomic; see the code on the right.
  * Show in class how we can get 9 or 11!
  * Tanenbaum shows how this can lead to disaster for a printer spooler.

**Remark**: Homework solutions for ch1 are posted. They are protected by a password that I will give in class and will repeat in class any lecture that I am asked. However, I can't send it to the class list as that is public.

### 2.3.2 Critical Regions (Sections)

We must prevent interleaving sections of code that need to be atomic with
respect to each other. That is, the conflicting sections need **mutual
exclusion**. If process A is executing its critical section, it excludes
process B from executing its critical section. Conversely if process B is
executing its critical section, it excludes process A from executing its
critical section.

Tanenbaum gives four requirements for a critical section implementation.

  1. No two processes may be simultaneously inside their critical section.
  2. No assumption may be made about the speeds or the number of concurrent threads/processes.
  3. No process outside its critical section (including the entry and exit code) may block other processes.
  4. No process should have to wait forever to enter its critical section. 
    * I do **NOT** make this last requirement.
    * I just require that the system as a whole make progress (so not all processes are blocked).
    * Specifically, I require that if one process is ready to enter its critical section, **some** processes (possibly not the one now ready to enter) will eventually enter its critical section.
    * I refer to solutions that do not satisfy Tanenbaum condition as _unfair_, but nonetheless _correct_, solutions.
    * Stronger fairness conditions have also been defined.

### 2.3.3 Mutual exclusion with busy waiting

We will study only solutions of this kind. Note that higher level solutions,
e.g., having one process block when it cannot enter its critical are
**implemented** using busy waiting algorithms.

#### Disabling Interrupts

The operating system can choose not to preempt itself. That is, we could
choose not to preempt system processes (if the OS is client server) or
processes running in system mode (if the OS is self service). Forbidding
preemption within the operating system would prevent the problem above where
x<\--x+1 not being atomic crashed the printer spooler (assume the spooler is
part of the OS).

The way to prevent preemption of kernel-mode code is to disable interrupts.
Indeed, disabling (i.e., temporarily preventing) interrupts is often done for
exactly this reason. This is not, however, a complete solution.

  * It does not work for user-mode programs. So the Unix print spooler, which is a user-mode program would need another solution.
  * We do not want to block interrupts for too long or the system will seem unresponsive.
  * Disabling interrupts is insufficient if the system has several processors. 
    * The main line can be executing on both processors simultaneously so interrupts are not involved.
    * One processor cannot block interrupts on the other.

#### Software solutions for two processes

  

##### Lock Variables

The idea is that each process, before entering the critical section, sets a
variable that locks the other process out of the critical section.

    
    
      Initially:   P1wants = P2wants = false
    
      Code for P1                             Code for P2
    
      Loop forever {                          Loop forever {
         P1wants <-- true         ENTRY          P2wants <-- true
         while (P2wants) {}       ENTRY          while (P1wants) {}
         critical-section                        critical-section
         P1wants <-- false        EXIT           P2wants <-- false
         non-critical-section }                  non-critical-section }
    

Explain why this works.

But it is wrong!  
Why?

Let's try again. The trouble was that setting want before the loop permitted
us to get stuck. We had them in the wrong order!

    
    
      Initially P1wants=P2wants=false
    
      Code for P1                             Code for P2
    
      Loop forever {                          Loop forever {
         while (P2wants) {}       ENTRY          while (P1wants) {}
         P1wants <-- true         ENTRY          P2wants <-- true
         critical-section                        critical-section
         P1wants <-- false        EXIT           P2wants <-- false
         non-critical-section }                  non-critical-section }
    

Explain why this works.

But it is wrong again!  
Why?

##### Strict Alternation

Now let's try being polite and really take turns. None of this wanting stuff.

    
    
      Initially turn=1
      
      Code for P1                      Code for P2
    
      Loop forever {                   Loop forever {
         while (turn = 2) {}              while (turn = 1) {}
         critical-section                 critical-section
         turn <-- 2                       turn <-- 1
         non-critical-section }           non-critical-section }
    

This one forces alternation, so is not general enough. Specifically, it does
not satisfy condition three, which requires that no process in its non-
critical section can stop another process from entering its critical section.
With alternation, if one process is in its non-critical section (NCS) then the
other can enter the CS once but not again.

The first example violated rule 4 (the whole system blocked). The second
example violated rule 1 (both in the critical section. The third example
violated rule 3 (one process in the NCS stopped another from entering its CS).

##### The First Correct Solution

In fact, it took years (way back when) to find a correct solution. Many
earlier solutions were found and several were published, but all were wrong.
The first correct solution was found by a mathematician named Dekker, who
combined the ideas of turn and wants. The basic idea is that you take turns
when there is contention, but when there is no contention, the requesting
process can enter. It is very clever, but I am skipping it (I cover it when I
teach distributed operating systems in CSCI-GA.2251). Subsequently, algorithms
with better fairness properties were found (e.g., no task has to wait for
another task to enter the CS twice).

What follows is Peterson's solution, which also combines wants and turn to
force alternation only when there is contention. When Peterson's algorithm was
published, it was a surprise to see such a simple solution. In fact Peterson
gave a solution for any number of processes. A proof that the algorithm
satisfies our properties (including a strong fairness condition) for any
number of processes can be found in _Operating Systems Review_ Jan 1990, pp.
18-22.

    
    
      Initially P1wants=P2wants=false  and  turn=1
    
      Code for P1                        Code for P2
    
      Loop forever {                     Loop forever {
         P1wants <-- true                   P2wants <-- true
         turn <-- 2                         turn <-- 1
         while (P2wants and turn=2) {}      while (P1wants and turn=1) {}
         critical-section                   critical-section
         P1wants <-- false                  P2wants <-- false
         non-critical-section }             non-critical-section }
    

Start Lecture #9

#### The TSL Instruction (Hardware Assist test-and-set)

Tanenbaum calls this instruction test and set lock TSL.

I call it test and set (TAS) and define  
    TAS(b)     where b is a binary variable,  
to ATOMICALLY set b<-true and return the OLD value of b.

Of course it would be silly to return the new value of b since we know the new
value is true.

The word **atomically** means that the two actions performed by TAS(x),
testing x (i.e., returning its old value) and setting x (i.e., giving it the
value true) are inseparable. Specifically it is **not** possible for two
concurrent TAS(x) operations to both return false (unless there is also
another concurrent statement that sets x to false).

With TAS available, implementing a critical section for any number of
processes is easy.

    
    
      loop forever {
          while (TAS(s)) {}  ENTRY
          CS
          s<--false          EXIT
          NCS }
    

### 2.3.4 Sleep and Wakeup

**Note:** Tanenbaum presents both busy waiting (as above) and blocking (process switching) solutions. We study only busy waiting solutions, which are easier and used in the blocking solutions. Sleep and Wakeup are the simplest blocking primitives. Sleep voluntarily blocks the process and wakeup unblocks a sleeping process. However, it is far from clear how sleep and wakeup are implemented. Indeed, deep inside, they typically use TAS or some similar primitive. We will not cover these solutions.

**Homeworkg:** Explain the difference between busy waiting and blocking process synchronization.

### 2.3.5 Semaphores

**Terminology note:** Tannenbaum use the term semaphore _only_ for blocking solutions. I will use the term for our busy waiting solutions (as well as for blocking solutions). Others call our solutions _spin locks_.

#### P and V

The entry code is often called P and the exit code V. Thus the critical
section problem is to write P and V so that the loop on the right satisfies:

    
    
      loop forever
         P
         critical-section
         V
         non-critical-section
    

  1. Mutual exclusion.
  2. No speed assumptions.
  3. No blocking by processes in NCS.
  4. Forward progress (my weakened version of Tanenbaum's last condition).

Note that, when writing pseudo-code, I use indenting carefully and hence do
not need (and sometimes omit) the braces {} used in languages like C or java.

#### Binary Semaphores

A **binary semaphore** abstracts the TAS solution we gave for the critical
section problem.

  * A binary semaphore S has two possible values open and closed (think of S as a gate (to a castle).
  * Two operations are supported.
  * P(S) is 
    
              while (S==closed) {}
          S<-closed     -- This is NOT the body of the while
        

where finding S=open and setting S<-closed is a single _atomic_

  * (Very) informally, the process waits until the gate is open, then atomically  
runs through and closes the gate.

  * Said yet another way, it is not possible for two processes doing P(S) simultaneously to both see S=open (unless a V(S) is also simultaneous with both of them).
  * V(S) is simply S<-open

The above code is _not_ real, i.e., it is _not_ an implementation of P. It
requires a sequence of two instructions to be atomic and that is, after all,
what we are trying to implement in the first place. The above code is,
instead, a _definition_ of the effect P is to have.

To repeat: for any number of processes, the critical section problem can be
solved using P and V as follows.

    
    
      loop forever
         P(S)
         CS
         V(S)
         NCS
    

The only solution we have seen for an arbitrary number of processes is the one
just before 2.3.4 with P(S) implemented via test and set.

**Note**: Peterson's solution requires each process to know its process number; the TAS soluton does not. Moreover the definition of P and V does not permit use of the process number. Thus, strictly speaking Peterson did not provide an implementation of P and V. He did, however, solve the critical section problem.

Start Lecture #10

#### Counting (or Generalized) Semaphores

To solve other coordination problems we want to extend binary semaphores.

  * With binary semaphores, two consecutive Vs do not permit two subsequent Ps to succeed (the gate cannot be doubly opened).
  * We might want to limit the number of processes in the section to 3 or 4, not always just 1.

Both of these (related) shortcomings can be overcome by not restricting
ourselves to a _binary_ variable, but instead define a **generalized** or
**counting** semaphore.

  * A counting semaphore S takes on non-negative integer values.
  * Two operations are supported.
  * P(S) is 
    
              while (S==0) {}
          S--
        

where finding S>0 and decrementing S is _atomic_

  * That is, wait until the gate is open (positive), then atomically run through and partially close the gate.
  * Another way to describe this atomicity is to say that it is not possible for the decrement to occur when S=0 and it is also not possible for two processes executing P(S) simultaneously to both see the same value of S unless a V(S) is also simultaneous.
  * V(S) is simply     S++

Counting semaphores can solve what I call the _semi-critical-section problem_,
where you permit up to k processes in the section. When k=1 we have the
original critical-section problem.

    
    
      initially S=k
    
      loop forever
         P(S)
         SCS   -- semi-critical-section
         V(S)
         NCS
    

#### Solving the Producer-Consumer Problem Using Semaphores

Recall that my definition of semaphore differs from Tanenbaum's; hence it is
not surprising that my solution to various coordination problems also differ
from his.

##### The Problem Statement

Unlike the previous problems of mutual exclusion where all processes are the
same, the producer-consumer problem has two classes of processes

  * Producers, which produce items and insert them into a buffer.
  * Consumers, which remove items from the buffer and consume them.

**Question**: What happens if a producer encounters a full buffer?  
**Answer**: It waits for the buffer to become non-full.

**Question**: What if a consumer encounters an empty buffer?  
**Answer**: It waits for the buffer to become non-empty.

The producer-consumer problem is also called the **bounded buffer** problem,
which is another example of active entities being replaced by a data structure
when viewed at a lower level (Finkel's level principle).

##### A Solution

Let k be the size of the buffer (the number of slots). Let e be a counting
semaphore (representing the number of empty slots), and let f be a counting
semaphore (representing the number of full slots).

    
    
    Initially e=k, f=0 (counting semaphores)
              b=open (binary semaphore)
     
    Producer                      Consumer
     
    loop forever                  loop forever
       produce-item                  P(f)
       P(e)                          P(b); take item from buf; V(b)
       P(b); add item to buf; V(b)   V(e)
       V(f)                          consume-item
    

We assume the buffer itself is only serially accessible. That is, only one
operation can be done at a time. This explains the P(b) V(b) around buffer
operations.

I use ; and put three statements on one line to suggest that a buffer
insertion or removal is viewed as one atomic operation. Of course this writing
style is only a convention, the enforcement of atomicity is done by the P/V.

The P(e), V(f) motif is used to force bounded alternation. If k=1 it gives
strict alternation.

### 2.3.6 Mutexes

**Remark:** Whereas we use the term semaphore to mean binary semaphore and explicitly say generalized or counting semaphore for the positive integer version, Tanenbaum uses semaphore for the positive integer solution and mutex for the binary version. Also, as indicated above, for Tanenbaum semaphore/mutex implies a blocking primitive; whereas I use binary/counting semaphore for both busy-waiting and blocking implementations. Finally, remember that in this course our **only** solutions are busy-waiting.

My Terminology

Busy waitblock/switch

critical

(binary) semaphore

(binary) semaphore

semi-critical

counting semaphore

counting semaphore

Tanenbaum's Terminology

Busy waitblock/switch

critical

enter/leave region

mutex

semi-critical

no name

semaphore

#### Mutexes in Pthreads

### 2.3.7 Monitors

### 2.3.8 Message Passing

### 2.3.9 Barriers

You can find some information on barriers in my [ lecture notes
](/~gottlieb/courses/1997-98-spring/os/class-notes.html) for a follow-on
course (see in particular lecture number 16).

## 2.5 Classical IPC Problems

### 2.5.0 The Producer-Consumer (or Bounded Buffer) Problem

We did this previously.

### 2.5.1 The Dining Philosophers Problem

A classic problem from Dijkstra concerning philosophers each of whose life
consists of  
loop forever

  * Think
  * Get hungry
  * Eat

Eating consists of the following

  * Up to 5 philosophers sitting at a round table.
  * Each philosopher has a plate of spaghetti.
  * There is a fork between each two philosophers.
  * Need two forks to eat.

What algorithm do you use for access to the shared resource (the forks)?

  * The obvious solution (pick up right; pick up left) deadlocks.
  * Big lock around everything serializes.
  * Good code in the book.

The purpose of mentioning the Dining Philosophers problem without giving the
solution is to give a feel of what coordination problems are like. The book
gives others as well. The solutions would be covered in a sequel course. If
you are interested look, for example
[here](/~gottlieb/courses/1997-98-spring/os/class-notes.html).

**Homework:** 51 and 55 (these have short answers but are not easy).

### 2.5.2 The Readers and Writers Problem

As in the producer-consumer problem we have two classes of processes.

  * Readers, which can work concurrently.
  * Writers, which need exclusive access.

The problem is to

  1. prevent 2 writers from running concurrently.
  2. prevent a reader and a writer from running concurrently.
  3. permit readers to be concurrent when no writer is active.
  4. (perhaps) insure fairness (e.g., freedom from starvation).

Variants

  * Writer-priority readers/writers.
  * Reader-priority readers/writers.

Solutions to the readers-writers problem are quite useful in multiprocessor
operating systems and database systems. The easy way out is to treat all
processes as writers in which case the problem reduces to mutual exclusion (P
and V). The disadvantage of the easy way out is that you give up reader
concurrency. Again for more information see the web page referenced above.

## 2.5A Critical Sections versus Database Transactions

Critical Sections have a form of atomicity, in some ways similar to
transactions. But there is a key difference: With critical sections you have
certain blocks of code, say A, B, and C, that are mutually exclusive (i.e.,
are atomic with respect to each other) and other blocks, say D and E, that are
mutually exclusive; but blocks from different critical sections, say A and D,
are _not_ mutually exclusive.

The day after giving this lecture in 2006-07-spring, I found a modern
reference to the same question. The quote below is from Subtleties of
Transactional Memory Atomicity Semantics by Blundell, Lewis, and Martin in
_Computer Architecture Letters_ (volume 5, number 2, July-Dec. 2006, pp.
65-66). As mentioned above, busy-waiting (binary) semaphores are often called
locks (or spin locks).

> ... conversion (of a critical section to a transaction) broadens the scope
of atomicity, thus changing the program's semantics: a critical section that
was previously atomic only with respect to other critical sections guarded by
the same lock is now atomic with respect to _all_ other critical sections.

## 2.5B: Summary of 2.3 and 2.5

We began with a subtle bug (wrong answer for x++ and x--) and used it to
motivate the **Critical Section Problem** for which we provided a (software)
solution.

We then defined **(binary) Semaphores** and showed that a Semaphore easily
solves the critical section problem and doesn't require knowledge of how many
processes are competing for the critical section. We gave an implementation
using **Test-and-Set**.

We then gave an operational definition of Semaphore (which is _not_ an
implementation) and morphed this definition to obtain a **Counting (or
Generalized) Semaphore**, for which we gave **NO** implementation. I asserted
that a counting semaphore can be implemented using 2 binary semaphores and
gave a reference.

We defined the **Producer-Consumer (or Bounded Buffer) Problem** and showed
that it can be solved using counting semaphores (and binary semaphores, which
are a special case).

Finally we briefly discussed some classical problems, but did not give (full)
solutions.

## 2.6 Research on Processes and Threads

Skipped.

## 2.7 Summary

Skipped, but you should read.

**Remark**: Chapter 2 homework solutions are on the web site. Password will be given again in class.

**Remark**: Midterm coming up. Could be next class but I think that is too soon. This is a big class for me to grade by the deadline so it must be the 22nd (next thursday).

# Chapter 6 Deadlocks

![gridlock](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/gridlock-crop-
shrink.png)  
![gridlock-new](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/gridlock-
new-crop.png)

**Note**: Deadlocks are closely related to process management so belong here, right after chapter 2. It was here in 2e. A goal of 3e is to make sure that the basic material gets covered in one semester. But I know we will do the first 6 chapters so there is no need for us to postpone the study of deadlock.

![deadlock](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/deadlock-
shrink.png)

**Definition**: A _deadlock_ occurs when every member of a set of processes is waiting for an event that can only be caused by a member of the set.

Often the event waited for is the release of a resource.

In the automotive world deadlocks are called _gridlocks_.

  * The processes are the cars.
  * The resources are the spaces on the street occupied by the cars.

For a computer science example consider two processes A and B that each want
to copy a file from a CD to a blank CD-R. Each processor needs exclusive
access to a CD reader and to a CD burner. Assume the system has exactly one of
each device.

It is quite possible for this to work perfectly. If A goes first, gets both
devices, does the copy, releases both devices, and the B does the same, all is
well.

However, the following problematic scenario is also possible.

  1. First, A obtains ownership of the burner (and will release it after getting the CD reader and copying the file).
  2. Then B obtains ownership of the CD reader (and will release it after getting the burner and copying the file).
  3. A now tries to get ownership of the drive, but is told to wait for B to release it.
  4. B now tries to get ownership of the burner, but is told to wait for A to release it.

**Bingo**: deadlock!

## 6.1 Resources

**Definition**: A _resource_ is an object that can be granted to a process.

### 6.1.1 Preemptable and Nonpreemptable Resources

Resources come in two types

  1. **Preemptable**, meaning that the resource can be taken away from its current owner (and given back later). An example is memory.
  2. **Non-preemptable**, meaning that the resource cannot be taken away. An example is a CD-burner.

The interesting issues arise with non-preemptable resources so those are the
ones we study.

The life history of a resource is a sequence of

  1. Request
  2. Allocate
  3. Use
  4. Release

Processes request the resource, use the resource, and release the resource.
The allocate decisions are made by the system and we will study policies used
to make these decisions.

### 6.1.2 Resource Acquisition

A simple example of the trouble you can get into.

  * Two resources and two processes.
  * Each process wants both resources.
  * Use a semaphore for each. Call them S and T.
  * If both processes execute  
`   P(S); P(T); <regular instructions> V(T); V(S)  
` all is well.

  * But if **one** executes instead  
`   P(T); P(S); <regular instructions> V(S); V(T)  
` disaster (deadlock can occur)! This was the CD-burner/CD-reader example just
above.

Recall from the semaphore/critical-section treatment last chapter, that it is
easy to cause trouble if a process dies or stays forever inside its critical
section. We assumed processes do not do this. Similarly, we assume that no
process retains a resource forever. It may obtain the resource an unbounded
number of times (i.e. it can have a loop with a resource request inside), but
each time it gets the resource, it must release it eventually.

## 6.2 Introduction to Deadlocks

Definition: A **deadlock** occurs when a every member of a set of processes is
waiting for an event that can only be caused by a member of the set.

Often the event waited for is the release of a resource.

### 6.2.1 (Necessary) Conditions for Deadlock

The following four conditions (Coffman; Havender) are _necessary_ but _not_
sufficient for deadlock. Repeat: They are not sufficient.

  1. **Mutual exclusion**: A resource can be assigned to at most one process at a time (no sharing).
  2. **Hold and wait**: A processing holding a resource is permitted to request another.
  3. **No preemption**: A process must release its resources; they cannot be taken away.
  4. **Circular wait**: There must be a chain of processes such that each member of the chain is waiting for a resource held by the next member of the chain.

One can say If you want a deadlock, you must have these four conditions.. But
of course you don't actually want a deadlock, so you would more likely say If
you want to prevent deadlock, you need only violate one or more of these four
conditions. .

The first three are static characteristics of the system and resources. That
is, for a given system with a fixed set of resources, the first three
conditions are either always true or always false: They don't change with
time. The truth or falsehood of the last condition does indeed change with
time as the resources are requested/allocated/released.

![resource-alloc](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/resource-
alloc.png)

### 6.2.2 Deadlock Modeling

On the right are several examples of a **Resource Allocation Graph**, also
called a **Reusable Resource Graph**.

  * The processes are circles.
  * The resources are squares.
  * An arc (directed line) from a process P to a resource R signifies that process P has requested, but has **not** yet been allocated, resource R.
  * An arc from a resource R to a process P indicates that process P has been allocated resource R and has not yet released it. We sometimes say that process P is _holding_ resource R.

**Homework:** 9\. Are all such reusable resource graphs legal?

Consider two concurrent processes P1 and P2 whose programs are.

    
    
      P1                   P2
      request R1           request R2
      request R2           request R1
      release R2           release R1
      release R1           release R2
    

On the board draw the resource allocation graph for various possible
executions of the processes, indicating when deadlock occurs and when deadlock
is no longer avoidable.

There are four strategies used for dealing with deadlocks.

  1. Ignore the problem.
  2. Detect deadlocks and recover from them.
  3. Prevent deadlocks by violating one of the 4 necessary conditions.
  4. Avoid deadlocks by carefully deciding when to allocate resources.

## 6.3 Ignoring the Problem--The Ostrich Algorithm

The put your head in the sand approach.

  * If the likelihood of a deadlock is sufficiently small and the cost of avoiding a deadlock is sufficiently high it might be better to ignore the problem. For example, if each PC deadlocks once per 10 years, the one reboot may be less painful that the restrictions needed to prevent it.
  * Clearly the ostrich algorithm is not suitable for nuclear missile launchers or for patient monitoring systems found in cardiac care units.
  * For embedded systems (such as the two examples above) the programs to be run are known in advance so many of the issues that occur in systems like Linux, MacOS or Windows (such as many processes wanting to fork at the same time) don't occur.

## 6.4 Deadlock Detection and Recovery

### 6.4.1 Detecting Deadlocks with One Resources of Each Type

Consider the case in which there is **only one** instance of each resource.

  * Thus a request can be satisfied by only one specific resource.
  * In **this case** the 4 necessary (Coffman-Havender) conditions for deadlock are also sufficient.
  * Remember we are making an assumption (single unit resources) that is often invalid. For example, many systems have several printers and a request is given for a printer not a specific printer. Similarly, one can have many CD-ROM drives.
  * In this special case the problem reduces to finding a directed cycle in the resource allocation graph.  
**Why**?  
**Answer**: Because the other three Coffman-Havender conditions are either always satisfied by the system we are studying (so we need only determine if condition 4 is satisfied), or are never satisfied by the system in question (in which case deadlock is impossible). That is, conditions 1,2,3 are static conditions on the system, not conditions on the state of the system right now.

To find a directed cycle in a directed graph is not hard. The algorithm is in
the book. The idea is simple.

  1. For each node in the graph do a depth first traversal to see if the graph is a DAG (directed acyclic graph), building a list as you go down the DAG (and pruning it as you backtrack back up).
  2. If you ever find the same node twice on your list, you have found a directed cycle, the graph is not a DAG, and deadlock exists among the processes in your current list.
  3. If you never find the same node twice, the graph is a DAG and no deadlock exists (right now).

The searches are finite since there are a finite number of nodes and you stop
if you hit a node twice.

### 6.4.2 Detecting Deadlocks with Multiple Unit Resources

![multiunit-graph](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams
/multiunit-graph.png)

This is more difficult.

  * The figure on the right shows a resource allocation graph with multiple unit resources.
  * Each unit is represented by a dot in the box.
  * Request edges are drawn to the box since they represent a request for **any** dot in the box.
  * Allocation edges are drawn from a dot to represent that a specific unit of the resource has been assigned (but all units of the resource are equivalent and the choice of which one to assign is arbitrary).
  * Note that there is a directed cycle shown in red, but there is no deadlock. Indeed the middle process might finish, erasing the cyan arc and permitting the blue dot to satisfy the rightmost process.
  * The book gives an algorithm for detecting deadlocks in this more general setting. The idea is as follows. 
    1. look for a process that **might** be able to terminate. That is, a process all of whose request arcs can be satisfied by resources the manager has on hand right now.
    2. If one such process is found, pretend that it **does** terminate (erase all its arcs), and repeat step 1.
    3. If any processes remain, they are deadlocked.
  * We will soon do in detail an algorithm (the Banker's algorithm) that has some of this flavor.
  * The algorithm just given makes the most _optimistic_ assumption possible about a non-blocked process: It will return all its resources and terminate normally. If we still find processes that remain blocked, they are deadlocked.
  * In the bankers algorithm we will make the most _pessimistic_ assumption possible about a running process: It immediately asks for all the resources it **can possibly** request (later we will explain in detail the meaning of can possibly). If, even with such demanding processes, the resource manager can insure that all process terminates, then the manager can insure that deadlock is avoided.

### 6.4.3 Recovery from deadlock

#### Recovery through Preemption

Perhaps you can temporarily preempt a resource from a process. Not likely.

#### Recovery through Rollback

Database (and other) systems take periodic checkpoints. If the system does
take checkpoints, one can roll back to a checkpoint whenever a deadlock is
detected. You must somehow guarantee forward progress.

#### Recovery through Killing Processes

Can always be done but might be painful. For example some processes have had
effects that can't be simply undone. Print, launch a missile, etc.

Start Lecture #11

**Remarks**

  1. Midterm Exam will be the Tuesday **after** spring break and will cover chapters 1, 2, and 6.
  2. A practice exam is on the home page.
  3. Solutions to chapter 1 homeworks are on NYU classes.
  4. There was no homework for lecture #8.
  5. The homework for lectures #9 and #10 is due Thursday, 3 March. Then I will post solutions to chapter 2 homeworks.
  6. The homework for lectures #11 and #12 will be due Tuesday, 8 March. Then I will post solutions to chapter 6 homeworks.
  7. I had tried to make lab 2 a little easier and removed () from the inputs. Unfortunately, I didn't removed them from the description of the problem. We will accept the lab either way. For example your lab may accept input-1 as either  
    1   0 1 5 1     or as     1   (0 1 5 1).  
If your lab 2 expects the () please say so in your README.

**Note**: We are doing 6.6 before 6.5 since 6.6 is easier and I believe serves as a good warm-up.

## 6.6: Deadlock Prevention

Attack one of the Coffman/Havender conditions.

### 6.6.1 Attacking the Mutual Exclusion Condition

The idea is to use spooling instead of mutual exclusion. Not possible for many
kinds of resources.

### 6.6.2 Attacking the Hold and Wait Condition

Require each processes to request all resources at the beginning of the run.
This is often called **One Shot**.

### 6.6.3 Attacking the No Preemption Condition

Normally not possible. That is, some resources are inherently pre-emptable
(e.g., memory). For those, deadlock is not an issue. Other resources are non-
preemptable, such as a robot arm. It is often not possible to find a way to
preempt one of these latter resources. One exception, which we shall not
study, is if the resource (say a CD-ROM drive) can be virtualized (recall
hypervisors).

### 6.6.4 Attacking the Circular Wait Condition

Establish a fixed ordering of the resources and require that they be requested
in this order. So if a process holds resources #34 and #54, it can request
only resources #55 and higher.

It is easy to see that a cycle is no longer possible.

**Homework:** 10\. Consider Figure 6-4. Suppose that in step (o) C requested S instead of requesting R. Would this lead to deadlock? Suppose that it requested both S and R.

## 6.5: Deadlock Avoidance

Let's see if we can tiptoe through the tulips and avoid deadlock states even
though our system does permit all four of the necessary conditions for
deadlock.

An _optimistic_ resource manager is one that grants every request as soon as
it can. To avoid deadlocks with all four conditions present, the manager must
be smart not optimistic.

### 6.5.1 Resource Trajectories

In this section we assume knowledge of the entire request and release pattern
of the processes _in advance_. Thus we are not presenting a practical
solution. I believe this material is useful as motivation for the more nearly
practical solution that follows, the Banker's Algorithm.

    
    
          H             V
      <reg code>    <reg code>
      P(print)      P(plot)
      <reg code>    <reg code>
      P(plot)       P(print)
      <reg code>    <reg code>
      V(print)      V(plot)
      <reg code>    <reg code>
      V(plot)       V(print)
      <reg code>    <reg code>
    

The diagram below depicts two processes H (horizontal) and V (vertical)
executing the programs shown on the right.

We plot progress of each process along an axis. In the example we show, there
are two processes, hence two axes, i.e., planar.

  * <reg code> signifies computation that neither requests nor releases any resources.
  * H first requests the printer; then requests the plotter; then uses both; and finally releases the plotter and then the printer
  * V requests the plotter first and releases the printer first.
  * The origin of the graph represents both processes starting.
  * Their combined state is a point on the graph.

The time periods where the printer and plotter are needed by each process are
indicated along the axes and their combined effect is represented by the
colors of the squares.

![trajectories](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/trajectorie
s.png)

  * The system starts at the lower left corner and the goal is to reach the upper right corner, where both processes have finished.
  * The dark green is where both processes have the plotter and hence execution cannot reach this area.
  * Light green represents both having the printer; also impossible.
  * Pink represents both processes having both printer and plotter, which is impossible.
  * Gold is possible (H has the plotter, V has the printer), but the system can't get there.
  * The cyan is safe. From anywhere in the cyan we have horizontal and vertical moves to the finish point without hitting any impossible area.
  * The brown dot is ... (cymbals) deadlock. We don't want to go there.
  * The magenta is very interesting. It is 
    * Possible: each processor has a different resource.
    * Reachable from the starting point.
    * Not deadlocked: each processor can move within the magenta.
    * Deadly: deadlock is unavoidable. The system will hit a magenta-green boundary and then will have no choice but to turn and go to the brown dot.
  * The cyan-magenta border is the danger zone.

The dashed line represents a possible execution pattern.

  * With a uniprocessor no diagonals are possible. We either move to the right meaning H is executing or move up indicating V is executing.
  * The trajectory shown represents. 
    1. H excuting a little.
    2. V excuting a little.
    3. H executes; requests the printer; gets it; executes some more.
    4. V executes; requests the plotter.

The crisis is at hand!

  * If the resource manager gives V the plotter, the magenta has been entered and all is lost. Abandon all hope ye who enter here--Dante.
  * The right thing to do is to deny the request, let H execute and move horizontally. While we are under the magenta, we must continue to refuse V even though the plotter is available.
  * Once we are under the dark green, we no longer have a choice: The plotter is no longer available so V's request cannot be granted.
  * At the end of the dark green, no danger remains, both processes will complete successfully. Victory!

This procedure is not practical for a general purpose OS since it requires
knowing the programs in advance. That is, the resource manager, knows in
advance what requests each process will make and in what order.

**Homework:** 17\. All the trajectories in the Figure are horizontal or vertical. Under what conditions is is possible for a trajectory to be a diagonal.

**Homework:** 18, 19.

### 6.5.2 Safe States

Avoiding deadlocks given some extra knowledge.

  * Not surprisingly, the resource manager knows how many units of each resource it had to begin with.
  * Also it knows how many units of each resource it has given to each process.
  * It would be great to see all the programs in advance and thus know all future requests, but that is asking for too much.
  * Instead, when each process starts, it announces its maximum usage. That is each process, before making any resource requests, tells the resource manager the maximum number of units of each resource the process can possible need. This is called the **claim** of the process. 
    * If the claim is greater than the total number of units in the system the resource manager kills the process when receiving the claim (or returns an error code so that the process can make a new claim).
    * If during the run the process asks for more than its claim, the process is aborted (or an error code is returned and no resources are allocated).
    * If a process claims more than it needs, the result is that the resource manager will be more conservative than need be and there will be more waiting.

**Definition**: A state is **safe** if there is an ordering of the processes such that: if the processes are run in this order, they will all terminate (assuming none exceeds its claim, and assuming each would terminate if all its requests are granted).

Recall the comparison made above between detecting deadlocks with multi-unit
resources and the banker's algorithm).

  * The deadlock detection algorithm makes the most _optimistic_ assumption possible about a running process, namely that the process will return all its resources and then terminate normally. If we still find processes that remain blocked, they are deadlocked.
  * The banker's algorithm will make the most _pessimistic_ assumption about a running process, namely that the process will immediately asks for all the resources it **can** (i.e., up to its initial claim). If, even with such demanding processes, the resource manager can assure that all process terminates, then we can ensure that deadlock is avoided.

In the definition of a safe state no assumption is made about the running
processes. That is, for a state to be safe, termination must occur no matter
what the processes do (providing each would terminate if run alone and each
never exceeds its claims). Making no assumption on a process's behavior is the
same as making the most pessimistic assumption.

**Remark**: When I say pessimistic I am speaking from the point of view of the resource manager. From the manager's viewpoint, the worst thing a process can do is request resources.

Give an example of each of the following four possibilities. A state that is

  1. Safe and deadlocked--not possible.
  2. Safe and not deadlocked--a trivial is example is a graph with no arcs.
  3. Not safe and deadlocked--easy (any deadlocked state).
  4. Not safe and not deadlocked--interesting.
![safe-or-not](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/safe-or-
not.png)

Is the figure on the right safe or not?

You can **NOT** tell until I give you the initial claims of the process.

For the figure on the right, if the initial claims are:

  * P: 1 unit of R and 2 units of S (written (1,2))
  * Q: 2 units of R and 1 unit of S (written (2,1))
the state in the figure is **NOT** safe.

But if the initial claims are instead:

  * P: 2 units of R and 1 units of S (written (2,1))
  * Q: 1 unit of R and 2 units of S (written (1,2))
the state in the figure **IS** safe.

Explain why this is so.

Please do not make the unfortunately common exam mistake to give an example
involving safe states without giving the claims. So if I ask you to draw a
resource allocation graph that is safe or if I ask you to draw one that is
unsafe, you **MUST** include the initial claims for each process. I often, but
not always, ask such a question and **every** time I have done so, several
students forgot to give the claims and hence lost points.

A manager can determine if a state is safe.

  * Since the manager know all the claims, it can determine the maximum amount of additional resources each process can request.
  * The manager knows how many units of each resource it has left.

The manager then follows the following procedure, which is part of **Banker's
Algorithms** discovered by Dijkstra, to determine if the state is safe.

  1. If there are no processes remaining, the state is **safe**.
  2. Seek a process P whose maximum additional request for each resource type is less than what remains for that resource type. 
    * If no such process can be found, then the state is **not safe**.
    * If such a P can be found, the banker (manager) knows that if it refuses all requests except those from P, then it will be able to satisfy all of P's requests.  
**Why?**  
**Answer:** Look at how P was chosen.
  3. The banker now pretends that P has terminated (since the banker knows that it can guarantee this will happen). Hence the banker pretends that all of P's currently held resources are returned. This makes the banker richer and hence perhaps a process that was not eligible to be chosen as P previously, can now be chosen.
  4. Repeat these steps.

#### Example 1

Consider the example shown in the table on the right.

A safe state with 22 units of one resource

processinitial claimcurrent alloc max add'l

X

3

1

2

Y

11

5

6

Z

19

10

9

Total

16

Available

6

  * One resource type R with 22 unit.
  * Three processes X, Y, and Z with initial claims 3, 11, and 19 respectively.
  * Currently the processes have 1, 5, and 10 units respectively.
  * Hence the manager currently has 6 units left.
  * Also note that the max additional needs for the processes are 2, 6, and 9 respectively.
  * So the manager cannot assure (with its **current** remaining supply of 6 units) that Z can terminate. But that is **not** the question.
  * This state is safe. 
    1. Use 2 units to satisfy X; now the manager has 7 units.
    2. Use 6 units to satisfy Y; now the manager has 12 units.
    3. Use 9 units to satisfy Z; done!

#### Example 2

This example is a continuation of example 1 in which Z requested 2 units and
the manager (foolishly?) granted the request.

An unsafe state with 22 units of one resource

processinitial claimcurrent alloc max add'l

X

3

1

2

Y

11

5

6

Z

19

12

7

Total

18

Available

4

  * Currently the processes have 1, 5, and 12 units respectively.
  * The manager has 4 units.
  * The max additional needs are 2, 6, and 7.
  * This state is unsafe 
    1. X is the only process whose maximum additional request can be satisfied at this point.
    2. So use 2 unit to satisfy X; now the manager has 5 units.
    3. Y needs 6 and Z needs 7 and we can't guarantee satisfying either request.
  * Note that we **were** able to find a process (X) that can terminate, but then we were stuck. So it is not enough to find one process. We must find a sequence of all the processes.

**Notes**:

  1. An unsafe state is **not** necessarily a deadlocked state. Indeed, for many unsafe states, if the manager gets lucky all processes will terminate successfully. Processes that are not currently blocked can terminate (instead of requesting more resources up to their initial claim, which is the worst case and is the case the manager prepares for). A safe state means that the manager can **guarantee** that no deadlock will occur (even in the worst case in which processes request as much as permitted by their initial claims.)
  2. When the banker determines that a state is safe, the banker has found an ordering of the processes for which it is guaranteed that all will terminate. There can be other good orderings as well. The banker is **not** committed to the ordering it has found.  
For example, the banker in example 1 found that the order X, Y, Z will
guarantee termination. However, if the next event is a request for 1 unit by
Y, the banker will grant that request because the resulting state is again
safe. This is explained further in the next section.

### 6.5.3 The Banker's Algorithm (Dijkstra) for a Single Resource

The algorithm is simple: Stay in safe states. For now, we assume that, before
execution begins, all processes are present and all initial claims have been
given. We will relax these assumptions at the end of the chapter.

In a little more detail the banker's algorithm is as follows.

  * Before execution begins, ensure that the system is safe. That is, check that no process claims more than the manager has. If the check fails, then the offending process is trying to claim more of some resource than exists in the system and hence cannot be guaranteed to complete even if run by itself. You might say that it can become deadlocked all by itself. The only thing the manager can do is to refuse to acknowledge the existence of the offending process.
  * When the manager receives a request, it **pretends** to grant it, and then checks if the resulting state is safe. If it is safe, the request is really granted; if it is not safe the process is blocked (that is, the request is held up).
  * When a resource is returned, the manager (politely thanks the process and then) checks to see if the first pending requests can be granted (i.e., if the result would now be safe). If so, the pending request is granted. Whether or not the request was granted, the manager checks to see if the next pending request can be granted, etc.

**Homework:** 21.

### 6.5.4 The Banker's Algorithm for Multiple Resources

At a high level the algorithm is identical to the one for a single resource
type: Stay in safe states.

But what is a safe state in this new setting?

The same definition (if processes are run in a certain order they will all
terminate).

Checking for safety is the same idea as above. The difference is that to tell
if there are enough free resources for a processes to terminate, the manager
must check that, for **all** resource types, the number of free units is at
least equal to the max additional need of the process.

**Homework:** Consider a system containing a total of 12 units of resource R and 24 units of resource S managed by the banker's algorithm. There are three processes P1, P2, and P3. P1's claim is 0 units of R and 12 units of S, written (0,12). P2's claim is (8,15). P3's claim is (8,20). Currently P1 has 4 units of S, P2 has 8 units of R, P3 has 8 units of S, and there are no outstanding requests.

  1. What is the largest number of units of S that P1 can request at this point that the banker will grant?
  2. If P2 instead of P1 makes the request, what is the largest number of units of S that the banker will grant?
  3. If P3 instead of P1 or P2 makes the request, what is the largest number of units of S that the banker will grant?

**Remark**: Go over the previous homework.

#### Limitations of the Banker's Algorithm

  * Often users don't know the maximum requests their process will make. They then estimate conservatively (i.e., use big numbers for the claim). This causes the manager becomes very conservative.
  * New processes arriving cause a problem (but not so bad as Tanenbaum suggests). 
    * The process's claim must be less than the total number of units of the resource in the system. If not, the process is not accepted by the manager.
    * Since the state without the new process is safe, so is the state with the new process! Just use the process order the banker had originally and put the new process at the end.
    * Insuring fairness (starvation freedom) needs a little more work, but isn't too hard either (once an hour stop taking new processes until all current processes finish).
  * A resource can become unavailable (e.g., a CD-ROM drive might break). This can result in an unsafe state and deadlock.

**Homework:** 26, 29, and 38. There is an interesting typo in 26. A has claimed 3 units of resource 5, but there are only 2 units in the entire system. Change the problem by having B both claim and be allocated 1 unit of resource 5.

## 6.7 Other Issues

### 6.7.1 Two-phase locking

This is covered extensively in a database text. We will skip it.

### 6.7.2 Communication Deadlocks

We have mostly considered actually hardware resources such as printers, but
have also considered more abstract resources such as semaphores.

There are other possibilities. For example a server often waits for a client
to make a request. But if the request msg is lost the server is still waiting
for the client and the client is waiting for the server to respond to the
(lost) last request. Each will wait for the other forever, a deadlock.

A solution to this communication deadlock would be to use a timeout so that
the client eventually determines that the msg was lost and sends another.

But it is not nearly that simple: The msg might have been greatly delayed and
now the server will get two requests, which could be bad, and is likely to
send two replies, which also might be bad.

This gives rise to the serious subject of communication protocols.

### 6.7.3 Livelock

Instead of blocking when a resource is not available, a process may (wait and
then) try again to obtain it. Now assume process A has the printer, and B the
CD-ROM, and each process wants the other resource as well. A will repeatedly
request the CD-ROM and B will repeatedly request the printer. Neither can ever
succeed since the other process holds the desired resource. Since no process
is blocked, this is not technically deadlock, but a related concept called
_livelock_.

### 6.7.4 Starvation

As usual FCFS is a good cure. Often this is done by priority aging and picking
the highest priority process to get the resource. Also can periodically stop
accepting new processes until all old ones get their resources.

## 6.8 Research on Deadlocks

## 6.9 Summary

Read.

**Remark**: End of material on midterm.

Start Lecture #12

# Chapter 3 Memory Management

Also called **storage management** or **space management**.

The memory manager must deal with the **storage hierarchy** present in modern
machines.

  * The hierarchy consists of registers (the highest level), cache, central memory, disk.
  * Various (hardware and software) memory managers move data from level to level of the hierarchy.
  * We are concerned with the central memory ↔ disk boundary.

The same questions are asked about the cache ↔ central memory boundary when
one studies computer architecture. Surprisingly, the terminology is almost
completely different!

  * When should we move data up to a higher level? 
    * Fetch on demand (e.g., demand paging, which is dominant now and which we shall study in detail).
    * Prefetch 
      * Read-ahead for file I/O.
      * Software or hardware prefetching.
      * Large cache lines and pages.
      * Extreme example. Entire job present whenever running.
  * Unless the top level has sufficient memory for the entire system, we must also decide when to move data down to a lower level. This is normally called evicting the data (from the higher level).
  * In OS we concentrate on the central-memory/disk layers and transitions.
  * In architecture we concentrate on the cache/central-memory layers and transitions (and use different terminology).

We will see in the next few weeks that there are three independent decision:

  1. Should we have segmentation.
  2. Should we have paging.
  3. Should we employ fetch on demand.

Memory management implements **address translation**.

  * Convert virtual addresses to physical addresses. 
    * Also called logical to real address translation.
    * A **virtual address** is the address expressed in the program.
    * A **physical address** is the address understood by the computer hardware.
  * The translation from virtual to physical addresses is performed by the **Memory Management Unit** or (MMU).
  * Another example of address translation is the conversion of _relative_ addresses to _absolute_ addresses by the linker.
  * The translation from virtual to physical addresses might be trivial (e.g., the identity). As we shall see, it is definitely not trivial in a modern general purpose OS.
  * The translation might be difficult (i.e., slow). 
    * Often includes addition/shift/mask--not too bad.
    * Often includes memory references. 
      * VERY serious.
      * Solution is to cache translations in a **Translation Lookaside Buffer** (TLB). Sometimes called a translation buffer (TB).

**Homework:** What is the difference between a physical address and a virtual address?

#### **When** is address translation performed?

  1. At program writing time 
    * Programmer explicitly states where everything goes.
    * No longer done.
  2. At compile time 
    * Compiler generates _physical_ addresses.
    * Requires knowledge of where the compilation unit will be loaded.
    * No linker.
    * Loader is trivial.
    * Primitive.
    * Rarely used (MSDOS .COM files).
  

  3. At link-edit time (the linker lab) 
    * Compiler 
      * Generates relative (a.k.a. relocatable) addresses for each compilation unit.
      * References external addresses.
    * Linkage editor 
      * Converts relocatable addresses to absolute (i.e., relocates relative addresses).
      * Resolves external references.
      * Must also converts virtual to physical addresses by knowing where the linked program will be loaded. Linker lab does this, but it is trivial since we assume the linked program will be loaded at 0.
    * Loader is still trivial.
    * Hardware requirements are small.
    * A program can be loaded only where specified and **cannot** move once loaded.
    * Not used much any more.
  

  4. At load time 
    * Similar to at link-edit time, but do **not** fix the starting address.
    * Program can be loaded anywhere.
    * Program can move but cannot be split.
    * Need modest hardware: base/limit registers.
    * Loader sets the base/limit registers.
    * No longer common.
  

  5. At execution time 
    * Addresses translated dynamically during execution.
    * Hardware needed to perform the virtual to physical address translation quickly.
    * Currently dominates.
    * Much more information later.

#### Extensions

  1. Dynamic Loading 
    * When executing a call, check if the module is loaded.
    * If it is not loaded, have a linking loader load it and update the tables to indicate that it now is loaded and where it is.
    * This procedure slows down all calls to the routine (not just the first one that must load the module) unless you rewrite code dynamically.
    * Not used much.
  

  2. Dynamic Linking. 
    * This is covered later.
    * Commonly used.

**Note:** I will place ** before each memory management scheme.

## 3.1 No Memory Management

The entire process remains in memory from start to finish and does not move.

The sum of the memory requirements of all jobs in the system cannot exceed the
size of physical memory.

![monoprogramming](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/monoprog
ramming.png)

#### Monoprogramming

The good old days when everything was easy.

  * No address translation done by the OS (i.e., address translation is _not_ performed dynamically during execution).
  * Either reload the OS for each job (or don't have an OS, which is almost the same), or protect the OS from the job. 
    * One way to protect (part of) the OS is to have it in ROM.
    * Of course, must have the OS (read-write) data in RAM.
    * Can have a separate OS address space that is accessible only in supervisor mode.
    * Might put just some drivers in ROM (BIOS).
  * The user employs **overlays** if the memory needed by a job exceeds the size of physical memory. 
    * Programmer breaks program into pieces.
    * A root piece is always memory resident.
    * The root contains calls to load and unload various pieces.
    * Programmer's responsibility to ensure that a piece is already loaded when it is called.
    * No longer used, but we couldn't have gotten to the moon in the 60s without it (I think).
    * Overlays have been replaced by dynamic address translation and other features (e.g., demand paging) that have the system support logical address sizes greater than physical address sizes.
    * Fred Brooks (leader of IBM's OS/360 project and author of The mythical man month) remarked that the OS/360 linkage editor was terrific, especially in its support for overlays, but by the time it came out, overlays were no longer used.

#### Running Multiple Programs Without a Memory Abstraction

This can be done via swapping if you have only one program loaded at a time. A
more general version of swapping is discussed below.

One can also support a limited form of multiprogramming, similar to MFT (which
is described next). In this limited version, the loader relocates all relative
addresses, thus permitting multiple processes to coexist in physical memory
the way your linker permitted multiple modules in a single process to coexist.

**Remark**: Midterm covers the notes through chapter 6\. Also labs 1 and 2. Not the programs in the labs but the OS concepts. Indeed both are on the practice exam.

![MFT](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/MFT.png)

#### **Multiprogramming with Fixed Partitions

Two goals of multiprogramming are to improve CPU utilization, by overlapping
CPU and I/O, and to permit short jobs to finish quickly.

  * This scheme was used by IBM for system 360 OS/MFT (multiprogramming with a fixed number of tasks).
  * An alternative would have a single input list instead of one queue for each partition. 
    * With this alternative, if there are no big jobs, one can use the big partition for little jobs.
    * The single list is not a queue since would want to remove the first job for each partition.
    * I don't think IBM did this.
  * You can think of the input lists(s) as the ready list(s) with a scheduling policy of run to completion in each partition.
  * Each partition was **mono**programmed, the **multi**programming occurred **across** partitions.
  * The partition boundaries are **not** movable (must reboot to move a job). 
    * So the partitions are of fixed size.
    * MFT can have large **internal fragmentation**, i.e., wasted space _inside_ a region of memory assigned to a process.
  * Each process has a single segment (i.e., the virtual address space is contiguous). We will discuss segments later.
  * The physical address space is also contiguous (i.e., the program is stored as one piece).
  * No sharing of memory between process.
  * No dynamic address translation.
  * OS/MFT is an example of address translation during load time. 
    * The system must establish addressability.
    * That is, the system must set a register to the location at which the process was loaded (the bottom of the partition).  Actually this is done with a user-mode instruction so could be called execution time, but it is only done once at the very beginning. 
    * This register (often called a base register by ibm) is part of the programmer visible register set. Soon we will meet base/limit registers, which, although related to the IBM base register above, have the important difference of being outside the programmer's control or view.
    * Also called **relocation**.
    * In addition, since the linker/assembler allow the use of addresses as data, the loader itself relocates these at load time.
  * Storage keys are used for protection. 
    * An alternative protection method is base/limit registers, which are discussed below.
    * An advantage of the base/limit scheme is that it is easier to move a job.
    * But MFT didn't move jobs so this disadvantage of storage keys is moot.

## 3.2 A Memory Abstraction: Address Spaces

### 3.2.1 The Notion of an Address Space

Just as the process concept creates a kind of abstract CPU to run programs
(each process acts as thought it is the only one running), the address space
creates a kind of abstract memory for programs to live in.

Addresses spaces do for processes, what you so kindly did for modules in the
linker lab: permit each to believe it has its own memory starting at address
zero.

#### Base and Limit Registers

Base and limit registers are additional hardware, invisible to the programmer,
that supports multiprogramming by automatically adding the base address (i.e.,
the value in the base register) to every relative address when that address is
accessed at run time.

In addition the relative address is compared against the value in the limit
register and if larger, the processes aborted since it has exceeded its memory
bound. Compare this to your error checking in the linker lab.

The base and limit register are set by the OS when the process starts.

### 3.2.2 Swapping

Moving an _entire_ processes between disk and memory is called **swapping**.

#### Multiprogramming with Variable Partitions

Both the **number** and **size** of the partitions change with time.

![MVT](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/MVT.png)

  * OS/MVT (multiprogramming with a varying number of tasks).
  * Also early PDP-10 OS.
  * A process still has only one segment (as with MFT). That is, the virtual address space is contiguous.
  * The physical address is also contiguous, that is, the process is stored as one piece in memory.
  * The process can be of any size up to the size of the machine and the process size can change with time.
  * A single ready list.
  * A process can move (might be swapped back in a different place).
  * This is dynamic address translation (i.e., during run time).
  * Must perform an addition on every memory reference (i.e. on every address translation) to add the start address of the partition (the base register).
  * The hardware used was called a DAT (dynamic address translation) box by IBM.
  * OS/MVT eliminates **Internal Fragmentation**, which is defined to be unusable space within a process.

    * Find a region the exact right size.
    * Not quite true, can't get a piece with 108755 bytes. Would get say 10880. But internal fragmentation is _much_ reduced compared to MFT. Indeed, we say that internal fragmentation has been eliminated.
  * Introduces **external fragmentation**, i.e., holes _outside_ any region of memory assigned to a process.
  * What do you do _if no hole is big enough_ for the request? 
    * Can compactify 
      * Transition from bar 3 to bar 4 in diagram below.
      * This is expensive.
      * Not suitable for real time (MIT ping pong).
    * Can swap out one process to bring in another, e.g., bars 5-6 and 6-7 in the diagram.
  * There are never two more holes than processes. Why? 
    * Because next to a process there might be a process or a hole but next to a hole there must be a process.
    * So can have runs of processes, but not of holes.
    * If following a process, one is equally likely to have a process or a hole, you get about twice as many processes as holes.
  * Base and limit registers are used. 
    * Storage keys would not good since compactifying or moving would require changing many keys.
    * Storage keys might need a fine granularity to permit the boundaries to move by small amounts (to reduce internal fragmentation). Hence many keys would need to be changed.

**Homework:** 3\. A swapping system eliminates holes by compaction. Assume a random distribution of holes and data segments, assume the data segments are much bigger than the holes, and assume a time to read or write a 32-bit memory word of 4ns. About how long does it take to compact 4 GB? For simplicity, assume that word 0 is part of a hole and the highest word in memory conatains valid data.

### 3.2.3 Managing Free Memory

#### The Placement Question

MVT Introduces the **Placement Question**. That is, into which hole
(partition) should one we place the process when several holes are big enough?

There are several possibilities, including best fit, worst fit, first fit,
circular first fit, quick fit, next fit, and Buddy.

  * First fit chooses the first eligible hole (i.e., the first one big enough).
  * Best fit doesn't waste big holes, but does leave slivers and is expensive to run. More expensive to run than first fit since keeps going after finding a hole bigger than the size needed. Tends to leave ``slivers''.
  * Worst fit avoids slivers, but quickly eliminates all big holes so a big job will require compaction.
  * Quick fit keeps lists of some common sizes (but has other problems, see Tanenbaum).
  * Buddy system 
    * Round request to next highest power of two (causes _internal fragmentation_).
    * Look in list of blocks this size (as with quick fit).
    * If list empty, go higher and split into buddies.
    * When returning coalesce with buddy.
    * Do splitting and coalescing recursively, i.e. keep coalescing until can't and keep splitting until successful.
    * See Tanenbaum (look in the index) or an algorithms book for more details.

A current favorite is circular first fit, also known as next fit.

  * Use the first hole that is big enough (first fit) but start looking where you left off last time.
  * Doesn't waste time constantly trying to use small holes that have failed before, but does tend to use many of the big holes, which can be a problem.

**Homework:** 4\. Consider a swapping system in which memory consists of the following hole sizes in memory order: 10MB, 4MB, 20MB, 18MB 7MB, 9MB, 12MB, and 15MB. Using first fit, Which hole is taken for successive segment requests of

  1. 12MB
  2. 10MB
  3. 9MB
Now repeat for best fit, worst fit, and next fit.

#### Implementing Free Memory

Buddy comes with its own implementation. How about the others?

##### Memory Management with Bitmaps

Divide memory into blocks and associate a bit with each block, used to
indicate if the corresponding block is free or allocated. To find a chunk of
size N blocks need to find N _consecutive_ bits indicating a free block.

The only design question is how much memory does one bit represent.

  * Big: Serious internal fragmentation.
  * Small: Many bits to store and process.
  

##### Memory Management with Linked Lists

Instead of a bit map, use a linked list of nodes where each node corresponds
to a region of memory either allocated to a process or still available (a
hole).

  * Each item on list gives the length and starting location of the corresponding region of memory and says whether it is a hole or Process.
  * The items on the list are not taken from the memory to be used by processes.
  * The list is kept in order of starting address.
  * Merge adjacent holes when freeing memory.
  * Use either a singly or doubly linked list.
  

##### Memory Management using Boundary Tags

See Knuth, _The Art of Computer Programming_ vol 1.

  * Use the same memory for list items as for processes.
  * Don't need an entry in linked list for the blocks in use, just the avail blocks are linked.
  * The avail blocks themselves are linked, not a node that points to an avail block.
  * When a block is returned, we can look at the boundary tag of the adjacent blocks and see if they are avail. If so they must be merged with the returned block.
  * For the blocks currently in use, just need a hole/process bit at each end and the length. Keep this in the block itself.
  * We do not need to traverse the list when returning a block can use boundary tags to find predecessor.

#### The Replacement Question

MVT also Introduces the **Replacement Question**. That is, which victim should
we swap out when we need to free up some memory?

This is an example of the suspend arc mentioned in process scheduling.

We will study this question more when we discuss demand paging in which case
we swap out only _part_ of a process.

Considerations in choosing a victim

  * Cannot replace a job that is _pinned_, i.e. whose memory is tied down. For example, if _Direct Memory Access_ (DMA) I/O is scheduled for this process, the job is pinned until the DMA is complete.
  * Victim selection is a medium term scheduling decision 
    * A job that has been blocked for a long time is a good candidate.
    * Often choose as a victim a job that has been in memory for a long time.
  * Another question is how long should it stay swapped out.
  * For demand paging, where swaping out a page is not as drastic as swapping out a job, choosing the victim is an important memory management decision and we shall study several policies.

**Notes:**

  1. So far the schemes presented so far have had two properties: 
    1. Each job is stored contiguously in memory. That is, the job is contiguous in _physical_ addresses.
    2. Each job cannot use more memory than exists in the system. That is, the virtual addresses space cannot exceed the physical address space.
  2. Tanenbaum now attacks the second item. I wish to do both and start with the first.
  3. Tanenbaum (and most of the world) uses the term paging to mean what I call demand paging. This is unfortunate as it mixes together two concepts. 
    1. Paging (dicing the address space) to solve the placement problem and essentially eliminate external fragmentation.
    2. Demand fetching, to permit the total memory requirements of all loaded jobs to exceed the size of physical memory.
  4. Most of the world uses the term virtual memory as a synonym for demand paging. Again I consider this unfortunate. 
    1. Demand paging is a fine term and is quite descriptive.
    2. Virtual memory should be used in contrast with physical memory to describe any virtual to physical address translation.

#### ** (Non-Demand) Paging

![paging](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/paging.png)

Paging is the simplest scheme to remove the requirement of contiguous physical
memory.

  * The program is logically divided into fixed size pieces called **pages**. This partitioning is invisible to the user. Tanenbaum (and others) sometimes calls pages **virtual pages**.
  * The real memory into similarly divided into fixed size pieces called **page frames** or simply **frames**.
  * The size of a page (the page size) equals the size of a frame (the frame size).
  * Sprinkle the pages into the frames.
  * Keep a table (called the **page table**) having an entry for each page. The **page table entry** or PTE for page p contains the number of the frame f that contains page p.

**Example:** Assume a decimal machine with page size = frame size = 1000.  
Assume PTE 3 contains 459.  
Then virtual address 3372 corresponds to physical address 459372.  
Referring to the diagram p#=3, f#=459, and offset=372.

Properties of (non-demand) paging (without segmentation).

  * The entire process must be memory resident to run.
  * No holes, i.e., no external fragmentation.
  * If there are 500 frames available and the page size is 4KB, then any job requiring ≤ 2MB will fit, even if the available frames are scattered over memory.
  * Hence (non-demand) paging is useful; indeed, it was used (but no longer).
  * Introduces internal fragmentation approximately equal to 1/2 the page size for every process (really every segment).
  * Can have a job unable to run due to insufficient memory and have some (but not enough) memory available. This is _not_ called external fragmentation since it is not due to memory being fragmented.
  * Eliminates the _placement_ question. All pages are equally good since don't have external fragmentation.
  * The _replacement_ question remains.
  * Since page boundaries occur at random points in the program and can change from run to run (the page size can change with no effect on the program--other than performance), pages are not appropriate units of memory to use for protection and sharing. Segmentation, which is discussed later, is sometimes more appropriate for protection and sharing.
  * However, most current OSes do not have segmentation so they use pages for protection and sharing. If all you have is a hammer, everything looks like a nail.
  * Virtual address space remains contiguous.

Address translation

  * Each memory reference turns into 2 memory references. 
    1. Reference the page table.
    2. Reference central memory.
  * This would be a disaster!
  * But it isn't done that way. Instead,the MMU caches page#->frame# translations. This cache is kept near the processor and can be accessed rapidly.
  * This cache is called a translation lookaside buffer (TLB) or translation buffer (TB).
  * For the above example, after referencing virtual address 3372, there would be an entry in the TLB containing the mapping 3->459.
  * Hence a subsequent access to virtual address 3881 would be translated to physical address 459881 without an extra memory reference. Naturally, a memory reference for location 459881 itself would be required.

Choice of page size is discuss below.

**Homework:** 7\. Using the page table of Fig. 3.9, give the physical address corresponding to each of the following virtual addresses.

  1. 20
  2. 4100
  3. 8300

## 3.3: Virtual Memory (meaning Fetch on Demand)

The idea is to enable a program to execute even if only the active portion of
its address space is memory resident. That is, we are to swap in and swap out
**portions** of a program and can run a program even if some (perhaps most) of
the program is **not** in memory.

In a crude sense this could be called automatic overlays.

Advantages

  * The system can run a program larger than the total physical memory, i.e., the virtual address size of the process can exceed the physical address size of the computer.
  * Even if each program is smaller than physical memory, the sum of the memory of all the running programs can exceed physical memory.
  * Fetch-on-demand likely increase the multiprogramming level since the total size of the active, i.e. loaded, programs (running + ready + blocked) can exceed the size of the physical memory.
  * Since some portions of a program are rarely if ever used, it is an inefficient use of memory to have them loaded all the time. Fetch-on-demand will not load them if not used and will (hopefully) unload them in favor of other portions if they are not used for a long time.
  * Simpler for the **user** than overlays or aliasing variables (older techniques to run large programs using limited memory).

Disadvantages

  * More complicated for the OS.
  * Execution time less predictable (depends on other jobs).
  * Can over-commit memory (more later).

#### The Memory Management Unit and Virtual to Physical Address Translation

The memory management unit is a piece of hardware in the processor that,
together with the OS, translates virtual addresses (i.e., the addresses in the
program) into physical addresses (i.e., real hardware addresses in the
memory). The memory management unit is abbreviated as and normally referred to
as the **MMU**.

(The idea of an MMU and virtual to physical address translation applies
equally well to non-demand paging and in olden days the meaning of paging and
virtual memory included that case as well. Sadly, in my opinion, modern usage
of the term paging and virtual memory are limited to fetch-on-demand memory
systems, typically some form of demand paging.)

![demand-paging](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/demand-
paging.png)

### ** 3.3.1 Paging (Meaning Demand Paging)

The idea is to fetch pages from disk to memory when they are referenced,hoping
to get the most actively used pages in memory. The choice of page size is
discussed below.

Demand paging is very common: More complicated variants, multilevel-level
paging and paging plus segmentation (both of which we will discuss), have been
used and the former dominates modern operating systems.

Started by the Atlas system at Manchester University in the 60s (paper by
Fortheringham).

Each PTE continues to contain the frame number if the page is loaded. But what
if the page is not loaded (i.e., the page exists only on disk)?

The PTE has a flag indicating if the page is loaded (can think of the X in the
diagram on the right as indicating that this flag is not set). If the page is
not loaded, the location on disk could be kept in the PTE, but normally it is
not (discussed below).

When a reference is made to a non-loaded page (sometimes called a non-existent
page, but that is a bad name), the system has a lot of work to do. (We give
more details below.)

  1. Choose a free frame, if one exists.
  2. What if there is no free frame?  
Make one!

    1. Choose a victim frame. This is the **replacement** question about which we will have **much** more to say latter.
    2. Write the victim back to disk if it is dirty.
    3. Update the victim PTE to show that it is not loaded.
    4. Now we have a free frame.
  3. Copy the referenced page from disk to the free frame.
  4. Update the PTE of the referenced page to show that it is loaded and give the frame number.
  5. Do the standard paging address translation (p#,off)->(f#,off).

Really not done quite this way as we shall see later

**Homework:** 14\. A machine has a 32-bit address space and an 8-KB page. The page table is entirely in hardware, with one 32-bit word per entry. When a process starts, the page table is copied to the hardware from memory, at one word every 100 nsec. If each process runs for 100 msec (including the time to load the page table), what fraction of the CPU time is devoted to loading the page tables?

### 3.3.2 Page tables

A discussion of page tables is also appropriate for (non-demand) paging, but
the issues are more important with demand paging for at least two reasons.

  1. The total size of the active processes is no longer limited to the size of physical memory. Since the total size of the processes is greater, the total size of the page tables is greater and hence concerns over the size of the page table are more acute.
  2. With demand paging an important question is the choice of a victim page to page out. Data in the page table can be useful in this choice.

We must be able access to the page table very quickly since it is needed for
every memory access.

![big-page-table](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/big-page-
table.png)

Unfortunate laws of hardware.

  * Big and fast are essentially incompatible.
  * Big and fast and low cost is hopeless.

So we can't just say, put the page table in fast processor registers, and let
it be huge, and sell the system for $1000.

The simplest solution is to put the page table in main memory as shown on the
right. However this solution seems to be both too slow and too big.

  * The solution seems too slow since all memory references now require two reference.
  * We will soon see how to largely eliminate the extra reference by using a TLB.
  * The solution seems too big. 
    * Currently we are considering _contiguous_ virtual addresses ranges (i.e., the virtual addresses have no holes).
    * One often puts the stack at one end of the virtual address space and the global (or static) data at the other end and let them grow towards each other.
    * The **virtual** memory in between is unused and can be enormous.
    * That does **not** sound so bad. Why should we care about virtual memory?
    * Since unused virtual memory can be huge (in address range), the page table, which is stored in **real** memory, will mostly contain unneeded PTEs.
    * This scheme worked fine when the maximum virtual address size was comparable in size with the total physical address space (e.g., the PDP-11 of the 1970s) but that is no longer the case.
  * A fix is to use multiple levels of mapping. We will see two examples below: multilevel page tables and segmentation plus paging.

#### Structure of a Page Table Entry

Each page has a corresponding page table entry (PTE). The information in a PTE
is used by the hardware and its format is machine dependent; thus the OS
routines that access PTEs are not portable. Information set by and used by the
OS is normally kept in other OS tables.

(Actually some systems, those with software TLB reload, do not require
hardware access to the page table.)

The page table is indexed by the page number; thus the page number is **not**
stored in the table.

The following fields are often present in a PTE.

  1. The _Frame Number_. This field is the main reason for the table. It gives the virtual to physical address translation. It is the only field in the page table for (non-demand) paging.
  2. The _Valid_ bit. This tells if the page is currently loaded (i.e., is in a frame). If the bit is set, the page is in memory and the frame number in the PTE is is valid It is also called the _presence_ or _presence/absence_ bit. If a page is accessed whose valid bit is unset, a _page fault_ is generated by the hardware.
  3. The _Modified_ or _Dirty_ bit. Indicates that some part of the page has been written since it was loaded. This is needed when the page is evicted so that the OS can tell if the page must be written back to disk.
  4. The _Referenced_ or _Used_ bit. Indicates that some word in the page has been referenced. Used to select a victim: unreferenced pages make good victims by the locality property (discussed below).
  5. _Protection_ bits. For example one can mark text pages as execute only. This requires that boundaries between regions with different protection are on page boundaries. Normally many consecutive (in logical address) pages have the same protection so many page protection bits are redundant. Protection is more naturally done with segmentation, but in many current systems, it is done with paging since the systems don't utilize segmentation (even though the hardware supports it).

**Question**: Why not store the disk addresses of non-resident pages in the PTE?  
**Answer**: On most systems the PTEs are accessed by the hardware automatically on a TLB miss (see immediately below). Thus the format of the PTEs is determined by the hardware and contains only information used on page hits. Hence the disk address, which is only used on page faults, is not present.

### 3.3.3 Speeding Up Paging

As mentioned above, the simple scheme of storing the page table in its
entirety in central memory alone appears to be both too slow and too big. We
address both these issues here, but note that a second solution (segmentation)
to the size question is discussed later.

####  Translation Lookaside Buffers (and General Associative Memory)

**Note:** Tanenbaum suggests that associative memory and translation lookaside buffer are synonyms. This is wrong. Associative memory is a general concept of which translation lookaside buffer is a specific example.

An **associative memory** is a _content addressable memory_. That is you
access the memory by giving the _value_ of some field (called the index) and
the hardware searches all the records and returns the record whose index field
contains the requested value.

For example

    
    
      Name  | Animal | Mood     | Color
      ======+========+==========+======
      Moris | Cat    | Finicky  | Grey
      Fido  | Dog    | Friendly | Black
      Izzy  | Iguana | Quiet    | Brown
      Bud   | Frog   | Smashed  | Green
    

If the index field is Animal and Iguana is given, the associative memory
returns

    
    
      Izzy  | Iguana | Quiet    | Brown
    

A **Translation Lookaside Buffer** or **TLB** is an associate memory where the
index field is the page number. The other fields include the frame number,
dirty bit, valid bit, etc.

Note that, unlike the situation with a the page table, the page number **is**
stored in the TLB; indeed it is the index field.

A TLB is _small and expensive_ but at least it is _fast_. When the page number
is in the TLB, the frame number is returned very quickly.

On a miss, a _TLB reload_ is performed. The page number is looked up in the
page table. The record found is placed in the TLB and a victim is discarded
(not really discarded, dirty and referenced bits are copied back to the PTE).
There is no placement question since all TLB entries are accessed at once and
hence are equally suitable. But there is a replacement question.

**Homework:** 22\. A computer whose processes have 1024 pages in their address spaces keeps its page tables in memory. The overhead required for reading a word from the page table is 5 nsec. To reduce this overhead, the computer has a TLB, which holds 32 (virtual page, physical page frame) pairs, and can do a look up in 1 nsec. What hit rate is needed to reduce the mean overhead to 2 nsec?

As the size of the TLB has grown, some processors have switched from single-
level, fully-associative, unified TLBs to multi-level, set-associative,
separate instruction and data, TLBs.

We are actually discussing caching, but using different terminology.

  * Page frames are a cache for pages (one could say that central memory is a cache of the disk).
  * The TLB is a cache of the page table.
  * Also the processor almost surely has a cache (most likely several) of central memory.
  * In all the cases, we have small-and-fast acting as a cache of big-and-slow. However what is big-and-slow in one level of caching, can be small-and-fast in another level.

#### Software TLB Management

The words above assume that, on a TLB miss, the MMU (i.e., hardware and not
the OS) loads the TLB with the needed PTE and then performs the virtual to
physical address translation.

Some newer systems do this in software, i.e., the OS **is** involved.

![2-level-page-tables](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/2
-level-page-table.png)

#### Multilevel Page Tables

Recall the diagram above showing the data and stack growing towards each
other. Most of the virtual memory is the unused space between the data and
stack regions. However, with demand paging this space does _not_ waste real
memory. But the single large page table **does** waste real memory.

The idea of multi-level page tables (a similar idea is used in Unix i-node-
based file systems, which we study later when we do I/O) is to add a level of
indirection and have a page table containing pointers to page tables.

  * Imagine one big page table, which we will (eventually) call the second level page table.
  * We want to apply paging to this large table, viewing it as simply memory not as a page table. So we (logically) cut it into pieces each the size of a page. Note that many (typically 1024 or 2048) PTEs fit in one page so there are far fewer of these pages than PTEs.
  * Now construct a _first level page table_ containing PTEs that point to the pages produced in the previous bullet.
  * This first level PT is small enough to store in memory. It contains one PTE for every page of PTEs in the 2nd level PT, which reduces space by a factor of one or two thousand.
  * But since we still have the 2nd level PT, we have made the world bigger not smaller!
  * Don't store in memory those 2nd level page tables all of whose PTEs refer to unused memory. That is _use demand paging on the (second level) page table_!

This idea can be extended to three or more levels. The largest I know of has
four levels. We will be content with two levels.

#### Address Translation With a 2-Level Page Table

For a two level page table the virtual address is divided into three pieces

    
    
      +-----+-----+-------+
      | P#1 | P#2 | Offset|
      +-----+-----+-------+
    

  * P#1 gives the index into the first level page table.
  * Follow the pointer in the corresponding PTE to reach the frame containing the relevant 2nd level page table.
  * P#2 gives the index into this 2nd level page table.
  * Follow the pointer in the corresponding PTE to reach the frame containing the (originally) requested page.
  * Offset gives the offset in this frame where the originally requested word is located.

Do an example on the board.

The VAX used a 2-level page table structure, but with some wrinkles (see
Tanenbaum for details).

Naturally, there is no need to stop at 2 levels. In fact the SPARC has 3
levels and the Motorola 68030 has 4 (and the number of bits of Virtual Address
used for P#1, P#2, P#3, and P#4 can be varied). More recently, x86-64 also has
4-levels.

#### Inverted Page Tables

For many systems the virtual address range is much bigger that the size of
physical memory. In particular, with 64-bit addresses, the range is 264 bytes,
which is 16 million terabytes. If the page size is 4KB and a PTE is 4 bytes, a
full page table would be 16 thousand terabytes.

A two level table would still need 16 terabytes for the first level table,
which is stored in memory. A three level table reduces this to 16 gigabytes,
which is still large and only a 4-level table gives a reasonable memory
footprint of 16 megabytes.

An alternative is to instead keep a table indexed by frame number. The content
of entry f contains the number of the page currently loaded in frame f. This
is often called a **frame table** as well as an **inverted page table**.

Now there is one entry per **frame**. Again using 4KB pages and 4 byte PTEs,
we see that the table would be a constant 0.1% of the size of real memory.

But on a TLB miss, the system must **search** the inverted page table, which
would be hopelessly slow except that some tricks are employed. Specifically,
hashing is used.

Also it is often convenient to have an inverted table as we will see when we
study global page replacement algorithms. Some systems keep both page and
inverted page tables.

## 3.4 Page Replacement Algorithms (PRAs)

These are solutions to the _replacement_ question. Good solutions take
advantage of _locality_ when choosing the victim page to replace.

  1. **Temporal locality**: If a word is referenced now, it is _likely_ to be referenced in the near future.  
This argues for _caching_ referenced words, i.e. keeping the referenced word
near the processor for a while.

  2. **Spatial locality**: If a word is referenced now, nearby words are _likely_ to be referenced in the near future.  
This argues for _prefetching_ words around the currently referenced word.

  3. Temporal and spacial locality are lumped together into **locality**: If any word in a page is referenced, each word in the page is likely to be referenced. So it is good to bring in the entire page on a miss and to keep the page in memory for a while.

When programs begin there is no history so nothing to base locality on. At
this point the paging system is said to be undergoing a cold start.

Programs exhibit phase changes in which the set of pages referenced changes
abruptly (similar to a cold start). An example would occurs in your linker lab
when you finish pass 1 and start pass 2. At the point of a phase change, many
page faults occur because locality is poor.

Pages belonging to processes that have terminated are of course perfect
choices for victims.

Pages belonging to processes that have been blocked for a long time are good
choices as well.

### Random PRA

A lower bound on performance. Any decent scheme should do better.

### 3.4.1 The Optimal Page Replacement Algorithm

Replace the page whose **next** reference will be furthest in the future.

  * Also called Belady's min algorithm.
  * Provably optimal. That is, no algorithm generates fewer page faults.
  * Unimplementable: Requires predicting the future.
  * Good upper bound on performance.

### 3.4.2 The Not Recently Used (NRU) PRA

Divide the frames into four classes and make a random selection from the
lowest nonempty class.

  0. Not referenced, not modified.
  1. Not referenced, modified.
  2. Referenced, not modified.
  3. Referenced, modified.

Assumes that in each PTE there are two extra flags R (for referenced;
sometimes called U, for used) and M (for modified, often called D, for dirty).

NRU is based on the belief that a page in a lower priority class is a better
victim, i.e., is less important.

  * If a page is not referenced, locality suggests that it probably will not referenced again soon and hence is a good candidate for eviction.
  * If a clean page (i.e., one that is not modified) is chosen to evict, the OS does not have to write it back to disk and hence the cost of the eviction is lower than for a dirty page.

Implementation

  * When a page is brought in, the OS resets R and M (i.e. R=M=0).
  * On a read, the hardware sets R.
  * On a write, the hardware sets R and M.

Old cartoons often had prisoners wearing broad horizontal stripes and using
sledge hammers to break up rocks.

This gives what I sometimes call the prisoner problem: If you do a good job of
making little ones out of big ones, but a poor job job of the reverse, you
soon wind up with all little ones.

In this case we do a great job setting R but rarely reset it. We need more
resets. Therefore, every k clock ticks, the OS resets all R bits.

**Question**: Why not reset M as well?  
**Answer**: If a dirty page has a clear M, we will not copy the page back to disk when it is evicted, and thus the only accurate version of the page will be lost!

What if the hardware doesn't set these bits?  
Answer: The OS can uses tricks. When the bits are reset, the PTE is made to
indicate that the page is not resident (which is a lie). On the ensuing page
fault, the OS sets the appropriate bit(s).

So now the R and M bits tell us the NRU class

  0. If R=M=0, the page has not been referenced (recently) and is not modified (clean).
  1. If R=0 and M=1, the page has not been referenced and has been modified (dirty).
  2. If R=1 and M=0, the page has been referenced and is clean.
  3. If R=1 and M=1, the page has been referenced and is dirty.

### 3.4.3 FIFO PRA

Simple algorithm. Basically, we try to be fair to the pages: the first one
loaded is the first one evicted.

The natural implementation is to have a queue of nodes each referring to a
resident page (i.e., pointing to a frame).

  * When a page is loaded, a node referring to the page is appended to the tail of the queue.
  * When a page needs to be evicted, the head node is removed and the page referenced is chosen as the victim.

This sound reasonable at first, but it is not a good policy. The trouble is
that a page referenced say every other memory reference and thus **very**
likely to be referenced soon will be evicted because we only look at the
**first** reference to a page, when we should be particularly interested in
**recent** references to the page.

### 3.4.4 Second chance PRA

Similar to the FIFO PRA, but altered so that a page recently referenced is
given a second chance.

  * When a page is loaded, a node referring to the page is appended to the tail of list queue. The list is maintained in apparent order of loading (i.e. apparently, but not really, FIFO) The R bit of the page is cleared.
  * When a page needs to be evicted, the head node is removed and the page referenced is the **potential** victim.
  * If the R bit is unset (the page hasn't been referenced recently), then the page **is** the victim.
  * If the R bit is set, the page is given a second chance. Specifically, the R bit is cleared, the time of loading is changed to NOW, and the node referring to this page is appended to the rear of the queue (so it appears to have just been loaded), and the current head node becomes the potential victim.
  * What if all the R bits are set?
  * We will move each page from the front to the rear and will arrive at the initial condition but with all the R bits now clear. Hence we will remove the same page as fifo would have removed, but will have spent more time doing so.
  * As in NRU we periodically clear all the R bits.

### 3.4.5 Clock PRA

Same algorithm as 2nd chance, but uses a better implementation, namely a
circular list with a single pointer serving as both head and tail pointer.

We assume that the most common operation is to choose a victim and replace it
by a new page.

  * We use a circular list for the nodes and have a pointer pointing to the head entry. Think of the list as the hours on a clock and the pointer as the hour hand. (Hence the name clock PRA.)
  * The operation we need to support efficiently is replace the oldest, unreferenced page by a given new page.
  * Examine the node pointed to by the clock hand. If the R bit of the corresponding page is set, we give the page a second chance: clear the R bit and set the time to NOW (so the page looks freshly loaded), advance the hand, and examine the next node.
  * Eventually we will reach a node whose R bit is clear. The corresponding page is the victim.
  * Replace the victim with the new page (may involve 2 I/Os as always).
  * Update the node to refer to this new page.
  * Move the hand forward another hour so that the new page is at the rear.

#### LIFO PRA

This is terrible! Why?  
Ans: All but the last frame are frozen once loaded so you can replace only one
frame. This is especially bad after a phase shift in the program as now the
program is references mostly new pages but only one frame is available to hold
them.

### 3.4.6 Least Recently Used (LRU) PRA

When a page fault occurs, choose as victim that page that has been unused for
the longest time, i.e. the one that has been least recently used.

LRU is definitely

  1. Implementable: The _past_ is knowable.
  2. Good: Simulation studies have shown this.
  3. Difficult. Essentially the system needs to either: 
    * Keep a time stamp in each PTE, updated **on each reference** and scan all the PTEs when choosing a victim to find the PTE with the oldest timestamp.
    * Keep the PTEs in a linked list in usage order, which means **on each reference** moving the corresponding PTE to the end of the list.

**Homework:** 28\. If FIFO page replacement is used with four page frames and eight pages, how many page faults will occur with the reference string 0172327103 if the four frames are initially empty? Now repeat this problem for LRU.

**Homework:** 36\. A computer has four page frames. The time of loading, time of last access, and the R and M bits for each page are shown below (the times in clock ticks).

PageLoadedLast ref.RM

0

126

280

1

0

1

230

265

0

1

2

140

270

0

0

3

110

285

1

1

  1. Which page will NRU replace?
  2. Which page will FIFO replace?
  3. Which page will LRU replace?
  4. Which page will second chance replace?

#### A Hardware Cutesy in Tanenbaum

A clever hardware method to determine the LRU page.

  * For n pages, keep an nxn bit matrix.
  * On a reference to page i, set row i to all 1s and column i to all 0s.
  * At any time the 1 bits in the rows are ordered by inclusion. I.e. one row's 1s are a subset of another row's 1s, which is a subset of a third. (Tanenbaum forgets to mention this.)
  * So the row with the fewest 1s is a subset of all the others and is hence least recently used.
  * This row also has the smallest value, when treated as an unsigned binary number. So the hardware can do a comparison of the rows rather than counting the number of 1 bits.
  * Cute, but still impractical.

### 3.4.7 Simulating (Approximating) LRU in Software

#### The Not Frequently Used (NFU) PRA

Keep a count of how frequently each page is used and evict the one that has
been the lowest score. Specifically:

  * Include a counter (and reference bit R) in each PTE.
  * Set the counter to zero when the page is brought into memory.
  * Every k clocks, perform the following for each PTE. 
    1. Add R to the counter.
    2. Clear R.
  * Choose as victim the PTE with lowest count.

Rcounter

1

10000000

0

01000000

1

10100000

1

11010000

0

01101000

0

00110100

1

10011010

1

11001101

0

01100110

#### The Aging PRA

NFU doesn't distinguish between old references and recent ones. The following
modification does distinguish.

  * Include a counter (and reference bit, R) in each PTE.
  * Set the counter to zero when the page is brought into memory.
  * Every k clock ticks, perform the following for each PTE. 
    1. Shift the counter right one bit.
    2. Insert R as the new high order bit of the counter.
    3. Clear R.
  * Choose as victim the PTE with lowest count.

Aging does indeed give more weight to later references, but an n bit counter
maintains data for only n time intervals; whereas NFU maintains data for at
least 2n intervals.

**Homework:** 30\. A small computer on a smart card has four page frames. At the first clock tick, the R bits are 0111 (page 0 is 0, the rest are 1). At subsequent clock ticks, the values are 1011, 1010, 1101, 0010, 1010, 1100 and 0001. If the aging algorithm is used with an 8-bit counter, give the values of the four counters after the last tick.

**Homework:** 42\. It has been observed that the number of instructions executed between page faults is directly proportional to the number of page frames allocated to a program. If the available memory is doubled, the mean interval between page faults is also doubled. Suppose that a normal instruction takes 1 us, but if a page fault occurs, it takes 2001 us. If a program takes 60 sec to run, during which time it gets 15,000 page faults, how long would it take to run if twice as much memory were available?

### 3.4.8 The Working Set Page Replacement Algorithm (Peter Denning)

#### The Working Set Policy

The goals are first to specify which pages a given process needs to have
memory resident in order for the process to run without too many page faults
and second to ensure that these pages are indeed resident.

But this is impossible since it requires predicting the future. So we again
make the assumption that the near future is well approximated by the immediate
past.

We measure time in units of memory references, so t=1045 means the time when
the 1045th memory reference is issued. In fact we measure time separately for
each process, so t=1045 really means the time when _this_ process made its
1045th memory reference.

**Definition**: **w(k,t)**, the **working set** at time t (with window k) is the set of pages referenced by the last k memory references ending at reference t.

The idea of the working set policy is to ensure that each process keeps its
working set in memory.

  * Allocate |w(t,k)| frames to each process. This number differs for each process and changes with time.
  * On a fault, evict a page not in the working set.
  * If a process is suspended and swapped out; the working set then can be used to say which pages should be brought back when the process is resumed.

Unfortunately, determining w(t,k) precisely is quite time consuming. It is
never done in real systems. Instead approximations are used as we shall see

**Homework:** Describe a process (i.e., a program) that runs for a long time (say hours) and always has a working set size less than 10. Assume k=100,000 and the page size is 4KB. The program need not be practical or useful.

**Homework:** Describe a process that runs for a long time and (except for the very beginning of execution) always has a working set size greater than 1000. Again assume k=100,000 and the page size is 4KB. The program need not be practical or useful.

The definition of Working Set is local to a process. That is, each process has
a working set; there is no system wide working set other than the union of all
the working sets of each process.

However, the working set of a single process has effects on the demand paging
behavior and victim selection of other processes. If a process's working set
is growing in size, i.e., |w(t,k)| is increasing as t increases, then we need
to obtain new frames from other processes. A process with a working set
decreasing in size is a source of free frames. We will see below that this is
an interesting amalgam of local and global replacement policies.

Interesting questions concerning the working set include:

  1. What value should be used for k?  
Experiments have been done and k is surprisingly robust (i.e., for a given
system, a fixed value works reasonably for a wide variety of job mixes).

  2. How should we calculate w(t,k)?  
Hard to do exactly so ...

... Various approximations to the working set, have been devised. We will
study two: Using virtual time instead of memory references (immediately
below), and Page Fault Frequency (part of section 3.5.1). In 3.4.9 we will see
the popular WSClock algorithm that includes an approximation of the working
set as well as several other ideas.

#### Using Virtual Time

Instead of counting memory references and declaring a page in the working set
if it was used within k references, we declare a page in the working set if it
was used in the past τ seconds. This is easier to do since the system already
keeps track of time for scheduling (and perhaps accounting). Note that the
time is measured only while this process is running, i.e., we are using
virtual time.

#### A Possible Working-Set Algorithm

What follows is a possible working-set algorithm using virtual time.

Use reference and modify bits R and M as described above. As usual, the OS
clears both bits when a page is loaded and clears R every m milliseconds. The
hardware sets M on writes and sets R on every access.

Add a field time of last use to the PTE. The procedure for setting this field
is below.

If the reference bit is 1, the page has been referenced within the last m
milliseconds, which we assume is significant shorter than τ seconds. Hence a
page with R=1 is in the working set.

To choose a victim when a page fault occurs (also setting the time of last use
field) we scan the page table and treat each resident page as follows. Since
we are interested only in resident pages, we would rather scan a page frame
table.

  * If the R bit is 1, the page is in the working set as we said above and hence is not evicted. We set its the time of last use to the current (virtual) time. This approximation can be wrong by at most m milliseconds.
  * If the R bit is 0, but the stored time of last use is less than τ seconds ago, the page is again in the working set so is not evicted.
  * If the R bit is 0 and the stored time of last use is more than τ seconds ago, the page is not in the working set and is evicted (but we keep scanning).
  * If no page was chosen for eviction, evict the page with R=0 that has the earliest time of last use.
  * If all pages have R=1, use some other method (say a random, preferably clean, page).

### 3.4.9 The WSClock Page Replacement Algorithm

The WSClock algorithm combines aspects of the working set algorithm (with
virtual time) and the clock implementation of second chance. It also
distinguishes clean from dirty and referenced from non-referenced in the
spirit of NRU.

As in clock we create a circular list of nodes with a hand pointing to the
next node to examine. There is one such node for every resident page of this
process; thus the nodes can be thought of as a list of frames or a kind of
inverted page table.

As in working set we store in each node the referenced and modified bits R and
M and the time of last use. R and M ar treated as above

  * R and M are cleared when the page is read in.
  * R is set by the hardware on a reference and cleared periodically by the OS (say every m milliseconds).
  * M is set by the hardware on a write.

We discuss below the setting of the time of last use and the clearing of M.

We use virtual time and declare a page old if its last reference is more than
τ seconds in the past. We again assume τ seconds is much longer than m
milliseconds. Other pages are declared young (i.e., in the working set).

As with clock, on every page fault a victim is found by scanning the list of
resident pages starting with the page indicated by the clock hand.

  * If R=1, the page has been recently referenced. As in second chance, R is set to 0, the time of last use is set to _now_, and the hand advances.
  * If R=M=0 and the page is old, this is our victim. Since the page is clean, we can start writing the new page immediately. Update the PTE and advance the hand. The algorithm has completed.
  * If R=M=0 and the page is young, the page is in the working set so is not evicted. Advance the hand and continue.
  * If R=0 and M=1, we have a dirty page that is not recently referenced (it might still be young, i.e., in the working set). We clear M, schedule an I/O to write the dirty page, and advance the hand.

It is possible to go all around the clock without finding a victim. In that
case

  * If writes were scheduled on old pages, one of these will become the victim once it becomes clean.
  * If no writes were scheduled, we will never find a victim (since nothing will change) so pick a page at random (or perhaps the oldest of the young pages).
  * If only young pages are scheduled for writing, again no victim will be chosen, and we pick a page at random (if every page is dirty, we must wait for one to become clean).

An alternative treatment of WSClock, including more details of its interaction
with the I/O subsystem, can be found [here](wsclock-davis.html).

### 3.4.10 Summary of Page Replacement Algorithms

  

AlgorithmComment

Random

Poor, used for comparison

Optimal

Unimplementable, used for comparison

NRU

Crude

FIFO

Not good ignores frequency of use

Second Chance

Improvement over FIFO

Clock

Better implementation of Second Chance

LIFO

Horrible, useless

LRU

Great but impractical

NFU

Crude LRU approximation

Aging

Better LRU approximation

Working Set

Good, but expensive

WSClock

Good approximation to working set

### 3.4.A Belady's Anomaly

Consider a system that has no pages loaded and that uses the FIFO PRU.  
Consider the following reference string (sequence of pages referenced by a
given process).

    
    
      0 1 2 3 0 1 4 0 1 2 3 4
    

What happens if we run the process on a tiny machine with only 3 frames? What
if we run it on a bigger (but still tiny) machine with 4 frames?

  * If we have 3 frames this generates 9 page faults (do it).
  * If we have 4 frames this generates 10 page faults (do it).
  * That's crazy! A bigger machine has **more** faults?!
  * That's why its called an anomaly!

Theory has been developed and certain PRA (so called stack algorithms) cannot
suffer this anomaly for any reference string. FIFO is clearly not a stack
algorithm. LRU is.

Repeat the above calculations for LRU.

**Note**: A former OS student, Alec Jacobson, has extended the above to a repeating string so that, if _N_ cycles of the repeating pattern are included, a FIFO replacement policy with 4 frames has _N_ more faults than one with only 3 frames. His blog entry is [here](http://www.alecjacobson.com/weblog/?p=746) and a local (de-blogged) copy is [here.](belady-jacobson.html)

## 3.5 Design Issues for (Demand) Paging Systems

###  3.5.1 Local vs Global Allocation Policies

A **local** PRA is one is which a victim page is chosen among the pages of the
same process that requires a new frame. That is the number of frames for each
process is fixed. So LRU for a local policy means that, on a page fault, we
evict the page least recently used by **this** process. A **global** policy is
one in which the choice of victim is made among all pages of all processes.

**Question**: Why is a purely local policy impractical/impossible.  
**Answer:** A new process has zero frames. With a purely local policy, the new process would never get a frame. More realistically, if you arranged for the first fault to be satisfied before restricting to purely local, a new process would remain with only one frame.

A more reasonable local policy would be to wait until a process has been
running a while before restricting it to existing frames or give the process
an initial allocation of frames based on the size of the executable.

In general, a global policy seems to work better. For example, consider LRU.
With a local policy, the local LRU page might have been **more** recently used
than many resident pages of other processes. A global policy needs to be
coupled with a good method to decide how many frames to give to each process.
By the working set principle, each process should be given |w(k,t)| frames at
time t, but this value is hard to calculate exactly.

If a process is given too few frames (i.e., well below |w(k,t)|), its faulting
rate will rise dramatically. If this occurs for many or all the processes, the
resulting situation in which the system is doing very little useful work due
to the high I/O requirements for all the page faults is called **thrashing**.

#### Page Fault Frequency (PFF)

An approximation to the working set policy that is useful for determining how
many frames a process needs (but not which pages) is the **Page Fault
Frequency** algorithm.

  * For each process keep track of the page fault frequency, which is the number of faults divided by the number of references.
  * Actually, must use a window or a weighted calculation since you are interested in the recent page fault frequency.
  * Actually, it is too expensive to calculate the number of references so, as above, we approximate this by the amount of (virtual) time.
  * If the PFF is exceptionally low, free some of this processes frames (e.g., limit victim selection to this process for a while).
  * If the PFF is too high, allocate more frames to this process. Either 
    1. Raise its number of frames if using a local policy; or
    2. Bar its frames from eviction (for a while) if using a global policy.

**Question**: What if there are not enough frames in the entire system? That is, what if the PFF is too high for all processes?  
**Answer**: Reduce the MPL as we now discuss.

### 3.5.2: Load Control

![process-states](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/process-
states.png)

To reduce the overall _memory pressure_, we must reduce the multiprogramming
level (or install more memory while the system is running, which is not
possible with current technology).

This gives a connection between memory management and process management.
These are the suspend/resume arcs we saw way back when and are shown again in
the diagram on the right.

When the PFF (or another indicator) is too high, we choose a process and
_suspend_ it, thereby swapping it to disk and releasing all its frames. When
the frequency gets low, we can _resume_ one or more suspended processes. We
also need a policy to decide when a suspended process should be resumed even
at the cost of suspending another.

This is called _medium-term scheduling_. Since suspending or resuming a
process can take seconds, we clearly do not perform this scheduling decision
every few milliseconds as we do for short-term scheduling. A time scale of
minutes would be more appropriate.

### 3.5.3: Page Size

**Question**: Why must the Page size be a multiple of the disk block size.  
**Answer**: When copying out a page if you have a partial disk block, you must do a read/modify/write (i.e., 2 I/Os).

Characteristics of a large page size.

  * Good for demand paging I/O: 
    * We will learn later this term that the total time for performing 8 I/O operations each of size 1KB is much larger that the time for a single 8KB I/O. Hence it is better to swap in/out one big page than several small pages.
    * But if the page is too big you will be swapping in data that are not local and hence might well not be used.
  * Large internal fragmentation (1/2 page size).
  * Small page table (process size / page size * size of PTE).
  * These last two can be analyzed together by setting the derivative of the sum equal to 0. The minimum overhead occurs at a page size of 
    
              sqrt(2 * process size * size of PTE)
        

Since the term inside the sqrt is typically millions of byte2, we see that
modern practice of having the page size a few kilobytes is near the minimum
point.

  * A very large page size leads to very few pages. A process will have many faults if it references more regions than the number of (large) frames that the process has been allocated.

A small page size has the opposite characteristics.

**Homework:** Consider a 32-bit address machine using paging with 8KB pages and 4 byte PTEs. How many bits are used for the offset and what is the size of the largest page table? Repeat the question for 128KB pages.

### 3.5.4: Separate Instruction and Data (I and D) Spaces

This was used when machine have very small virtual address spaces.
Specifically the PDP-11, with 16-bit addresses, could address only 216 bytes
or 64KB, a severe limitation. With separate I and D spaces there could be 64KB
of instructions and 64KB of data.

Separate I and D are no longer needed with modern architectures having large
address spaces.

### 3.5.5 Shared pages

Permit several processes to each have the same page loaded in the same frame.
Of course this can only be done if the processes are using the same program
and/or data.

  * Really should share segments.
  * Must keep reference counts or something so that, when a process terminates, pages it shares with another process are not automatically discarded.
  * Similarly, a reference count would make a widely shared page (correctly) look like a poor choice for a victim.
  * A good place to store the reference count would be in a structure pointed to by both PTEs. If stored in the PTEs themselves, we must somehow keep the count consistent among processes.
  * If you want the pages to be initially shared for reading but want each process's updates to be private, then use so called copy on write techniques.

**Homework:** Can a page shared between two processes be read-only for one process and read-write for the other? 

### 3.5.6 Shared Libraries (Dynamic-Linking)

In addition to sharing individual pages, process can share entire library
routines. The technique used is called **dynamic linking** and the objects
produced are called **shared libraries** or **dynamically-linked libraries
(DLLs)**. (The traditional linking you did in lab1 is today often called
**static linking**).

  * With dynamic linking, frequently used routines are not linked into the program. Instead, just a stub is linked.
  * When the routine is called (or when the process begins), the stub checks to see if the real routine has been loaded by _another_ program). 
    * If it has not been loaded, load it (really page it in as needed).
    * If it is already loaded, _share_ it. The read-write data must be shared copy-on-write.
  * _Advantages_ of dynamic linking. 
    * Saves RAM: Only one copy of a routing is in memory even when it is used concurrently by many processes. For example even a big server with hundreds of active processes will have only one copy of printf in memory. (In fact with demand paging only part of the routine will be in memory.)
    * Saves disk space: Files containing executable programs no longer contain copies of the shared libraries.
    * A bug fix to a dynamically linked library fixes all applications that use that library, **without** having to relink these applications.
  * _Disadvantages_ of dynamic linking. 
    * New bugs in dynamically linked library infect all applications.
    * Applications change even when they haven't changed.
  * A _Technical Difficulty_ with dynamic linking. The shared library has different _virtual_ addresses in each process so addresses relative to the beginning of the module cannot be used (they would need to be relocated to different addresses in the multiple copies of the module). Instead _position-independent code_ must be used. For example, jumps within the module would use PC-relative addresses. 

### 3.5.7 Mapped Files

The idea of **memory-mapped files** is to use the mechanisms in place for
demand paging (and segmentation, if present) to implement I/O.

A system call is used to map a file into a portion of the address space. (No
page can be part of a file and part of regular memory; the mapped file would
be a complete segment if segmentation is present).

The implementation of demand paging we have presented assumes that the entire
process is stored on disk. This portion of secondary storage is called the
backing store for the pages. Sometimes it is called a paging disk. For memory-
mapped files, the file itself is the backing store.

Once the file is mapped into memory, reads and writes become loads and stores.

### 3.5.8 Cleaning Policy (Paging Daemons)

In practice there is rarely no free frame to because many systems use a
_paging daemon_, a process that, whenever active, evicts pages to increase the
number of free frames. The daemon is activated when the number of free pages
falls below a low water mark and suspended when the number rises above a high
water mark.

Some replacement algorithm must be chosen, and naturally dirty pages must be
written back to disk prior to eviction.

Since we have studied replacement algorithms, we can suggest an implementation
of the daemon. If a clock-like algorithm is used for victim selection, one can
have a two handed clock with one hand (the paging daemon) staying ahead of the
other (the one invoked by the need for a free frame).

The front hand simply writes out any page it hits that is dirty and thus the
trailing hand is likely to see clean pages and hence is more quickly able to
find a suitable victim.

Note that our WSClock implementation had a page cleaner built in (look at the
implementation when R=0 and M=1).

_Unless specifically requested_, you may ignore paging daemons when answering
exam questions.

### 3.5.9 Virtual Memory Interface

Skipped.

## 3.6 Implementation Issues

### 3.6.1 Operating System Involvement with Paging

When must the operating system be involved with demand paging?

  * During process creation. The OS must allocate a page table and a region on disk to hold the pages that are not memory resident. A few pages of the process must be loaded.
  * The Ready->Running transition. Real memory must be allocated for the page table if the table has been swapped out (which is permitted when the process is not running).  
Some hardware register(s) must be set to point to the page table. There can be
many page tables resident (since there are many ready processes), but the
hardware must be told the location of the page table for the running process--
the active page table.  
The TLB must be cleared (unless it contains a process id field).

  * Processing a page fault. Much OS effort is needed; see 3.6.2 just below.
  * Process termination. Free the page table (and the disk region for swapped out pages, see below.

### 3.6.2 Page Fault Handling

What happens when a process, say process A, gets a page fault? Compare the
following with the processing for a trap command and for an interrupt.

  1. The hardware detects the fault and traps to the kernel (switches to supervisor mode and saves state).
  2. Some assembly language code saves more state, establishes the C-language (or another programming language) environment, and calls the OS.
  3. The OS determines that a page fault occurred and which page was referenced.
  4. If the virtual address is invalid, process A is killed. If the virtual address is valid, the OS must find a free frame. If there is no free frames, the OS selects a victim frame. (Really, the paging daemon does this prior to the fault occurring, but it is easier to pretend that it is done here.) Call the process owning the victim frame, process B. (If the page replacement algorithm is local, then B=A.)
  5. The PTE of the victim page is updated to show that the page is no longer resident.
  6. If the victim page is dirty, the OS schedules an I/O write to copy the frame to disk and blocks A waiting for this I/O to occur.
  7. Assuming process A needed to be blocked (i.e., the victim page is dirty) the scheduler is invoked to perform a context switch. 
    * Tanenbaum forgot some here.
    * The process selected by the scheduler (say process C) runs.
    * Perhaps C is preempted for D or perhaps C blocks and D runs and then perhaps D is blocked and E runs, etc.
    * When the I/O to write the victim frame completes, a disk interrupt occurs. Assume processes C is running at the time.
    * Hardware trap / assembly code / OS determines I/O done.
    * The scheduler marks A as ready.
    * The scheduler picks a process to run, maybe A, maybe B, maybe C, maybe another processes.
    * At some point the scheduler does pick process A to run. Recall that at this point A is still executing OS code.
  8. Now the O/S has a free frame (this may be much later in wall clock time if a victim frame had to be written). The O/S schedules an I/O to read the desired page into this free frame. Process A is blocked (perhaps for the second time) and hence the process scheduler is invoked to perform a context switch.
  9. Again, another process is selected by the scheduler as above and eventually a disk interrupt occurs when the I/O completes (trap / asm / OS determines I/O done). The PTE in process A is updated to indicate that the page is in memory.
  10. The O/S may need to fix up process A (e.g., reset the program counter to re-execute the instruction that caused the page fault).
  11. Process A is placed on the ready list and eventually is chosen by the scheduler to run. Recall that process A is executing O/S code.
  12. The OS returns to the first assembly language routine.
  13. The assembly language routine restores registers, etc. and returns to user mode.

The user's program running as process A is **unaware** that any of this
occurred.

### 3.6.3 Instruction Backup

A cute horror story. The hardware support for page faults in the original
Motorola 68000 (the first microprocessor with a large address space) was
flawed. If a processor encountered a page fault, there wasn't always enough
information to figure out what to do so (for example did a register pre-
increment occur). That is, one could not safely restart an instruction. This
was thought to make demand paging impossible.

However, one clever system for the 68000 used two processors, one executing
the program and a second processor executing one instruction behind. When a
page fault occurs the executing processor brings in the page and switches to
the second processor, which had not yet executed the instruction, thus
eliminating instruction restart and thereby supporting demand paging.

The next generation machine, the 68010, provided extra information on the
stack so the horrible/clever 2-processor kludge/hack was no longer necessary.

Don't worry about instruction backup; it is very machine dependent and all
modern implementations get it right.

### 3.6.4 Locking (Pinning) Pages in Memory

We discussed pinning jobs already. The same (mostly I/O) considerations apply
to pages.

### 3.6.5 Backing Store

The issue is where on disk do we put pages that are not in frames.

  * For program text, which is presumably read only, a good choice is the file executable itself.
  * What if we decide to keep the data and stack each contiguous on the backing store? Data and stack grow so we must be prepared to grow the space on disk, which leads to the same issues and problems as we saw with MVT.
  * If those issues/problems are painful, we can scatter the pages on the disk. That is, we can employ paging! Note that this is **not** demand paging.
  * This needs a table to specify where the backing space for each page is located. 
    * This corresponds to the page table used to tell where in real memory a page is located.
    * The format of the memory page table (the one we have studied up to now) is determined by the hardware since the hardware modifies/accesses it. It is machine dependent.
    * The format of the disk page table is decided by the OS designers and is machine independent.
    * If the format of the memory page table were flexible, then we could keep the disk information there as well. But normally the format is not flexible, and hence the disk information is not kept there.
  * What if we felt disk space was too expensive and wanted to put some of these disk pages on say tape or holographic storage?  
Ans: We use _demand paging_ of the disk blocks! That way "unimportant" disk
blocks will migrate out to tape and are brought back in if and when needed.  
Since a tape read requires _seconds_ to complete (because the request is not
likely to be for the sequentially next tape block), it is crucial that we get
**very** few disk block faults.  
I don't know of any systems that actually did this.

**Homework:** Assume every memory reference takes 0.1 microseconds to execute providing the reference page is memory resident. Assume a page fault takes 10 milliseconds to service providing the necessary disk block is actually on the disk. Assume a disk block fault takes 10 seconds service. So the worst case time for a memory reference is 10.0100001 seconds. Finally, assume the program requires that a billion memory references be executed.

  1. If the program is always completely resident, how long does it take to execute?
  2. If 0.1% of the memory references cause a page fault, but all the disk blocks are on the disk, how long does the program take to execute and what percentage of the time is the program waiting for a page fault to complete?
  3. If 0.1% of the memory references cause a page fault and 0.1% of the page faults cause a disk block fault, how long does the program take to execute and what percentage of the time is the program waiting for a disk block fault to complete?

### 3.6.6 Separation of Policy and Mechanism

Skipped.

## 3.7 Segmentation

Up to now, the **virtual** address space has been contiguous. In segmentation
the **virtual** address space is divided into a number of **variable**-size
pieces called _segments_. One can view the designs we have studied so far as
having just one segment, the entire address space of the process.

With just one segment (i.e., with all virtual addresses contiguous) memory
management is difficult when there are more that two dynamically growing
regions.

Imagine a program with several large, dynamically-growing, data structures.
The same problem we mentioned for the OS when there are more than two growing
regions, occurs as well here for user programs.

  * The user (or some user-mode tool) must decide how much virtual space to leave between the different data structures or the structures must be copied when they are grown. But it is not clear how far apart in virtual memory the data structures should be located, especially if in some runs, one of them gets extremely large but in other runs that structure is small but others are extremely large. (With just two data structures you start them on opposite sides of the virtual space and have them grow towards each other as we did before.) 
  * With segmentation the user instead gives each structure a different segment. That is, the system provides many virtual addresses spaces each starting at zero and the user place one structure in each.

This division of the address space is user _visible_. Recall that user visible
really means visible to user-mode programs.

Unlike (user-invisible) page boundaries, segment boundaries are specified by
the user and thus can be made to occur at logical points, e.g., one table per
segment..

Segmentation eases flexible protection and sharing: One places in a single
segment a unit that is logically shared. This would be a natural method to
implement shared libraries.

When shared libraries are implemented on paging systems, the design
essentially mimics segmentation by treating a collection of pages as a
segment. This requires that the end of the unit to be shared occurs on a page
boundary (this is done by padding).

Without segmentation (equivalently said with just one segment) all procedures
are packed together so, if one changes in size, all the virtual addresses
following this procedure are changed and the program must be re-linked. With
each procedure in a separate segment this relinking would be limited to the
symbols defined or used in the modified procedure.

**Homework:** Explain the difference between internal fragmentation and external fragmentation. Which one occurs in paging systems? Which one occurs in systems using pure segmentation?

#### ** Two Segments

Late PDP-10s and TOPS-10

  * Each process has one _shared_ text segment, that can also contain shared (normally read only) data. As the name indicates, all process running the same executable share the same text segment.
  * The process also contains one (private) writable data segment.
  * Permission bits defined for each segment.
![3-segments](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/3-segments.pn
g)

#### ** Three Segments

Traditional (early) Unix had three segments as shown on the right.

  1. Shared text marked execute only.
  2. Data segment (global and static variables).
  3. Stack segment (automatic variables).

Since the text doesn't grow, this was sometimes treated as 2 segments by
combining text and data into one segment. But then the text could not be
shared.

#### ** General (Not Necessarily Demand) Segmentation

Segmentation is a **user-visible** division of a process into multiple
**variable-size** segments, whose sizes **change dynamically** during
execution. It enables fine-grained sharing and protection. For example, one
can share the text segment as done in early unix.

With segmentation, the **virtual** address has two components: the segment
number and the offset in the segment.

Segmentation does **not** mandate how the program is stored in memory.

  * One possibility is that the entire program must be in memory in order to run it. Use whole process swapping. That is either all the segments of a process are memory resident or all of them are swapped ot. Early versions of Unix did this.
  * Can also implement demand segmentation (see below).
  * More recently, segmentation is combined with demand paging (see below).

All segmentation implementations employed a segment table with one entry for
each segment.

  * A segment table is similar to a page table.
  * Entries are called STEs, Segment Table Entries.
  * Each STE contains the physical base address of the segment and the limit value (the size of the segment).
  * Why is there no limit value in a PTE?  
**Answer**: All pages are the same size so the limit is obvious.

The address translation for segmentation is  
    (seg#, offset) --> if (offset<limit) base+offset else error. 

### 3.7.1: Implementation of Pure Segmentation

Pure Segmentation means segmentation without paging.

Segmentation, like whole program swapping, exhibits external fragmentation
(sometimes called _checkerboarding_). (See the treatment of OS/MVT for a
review of external fragmentation and whole program swapping). Since segments
are smaller than programs (several segments make up one program), the external
fragmentation is not as bad as with whole program swapping. But it is still a
serious problem.

As with whole program swapping, compaction can be employed.

#### ** Demand Segmentation

Same idea as demand paging, but applied to segments.

ConsiderationDemand  
Paging Demand  
Segmentation

User (mode) aware

No

Yes

How many addr spaces

1

Many

VA size > PA size

Yes

Yes

Protect individual  
procedures separately

No

Yes

Accommodate elements  
with changing sizes

No

Yes

Ease user sharing

No

Yes

Why invented

let the VA  
size exceed  
the PA size

Sharing,  
Protection,  
Independent  
addr spaces

Internal fragmentation

Yes

No, in principle

External fragmentation

No

Yes

Placement question

No

Yes

Replacement question

Yes

Yes

  * If a segment is loaded, base and limit are stored in the STE and the valid bit is set in the STE.
  * The STE is accessed on each memory reference (not really, there is probably a TLB).
  * If the segment is not loaded, the valid bit is unset. The base and limit as well as the disk address of the segment are stored in an OS table.
  * A reference to a non-loaded segment generate a segment fault (analogous to page fault).
  * To load a segment, we must solve both the placement question and the replacement question. This is the same as loading a program in whole programming swapping. For paging, there is no placement question since all frames are exactly the right size.
  * Pure segmentation was once implemented by Burroughs in the B5500. I believe the implementation was in fact demand segmentation.
  * Neither pure segmentation nor demand segmentation is used in modern systems.

The table on the right compares _demand_ paging with _demand_ segmentation.
The portion above the double line is from Tanenbaum.

### ** 3.7.2 and 3.7.3 Segmentation With (Demand) Paging

These two sections of the book cover segmentation combined with demand paging
in two different systems. Section 3.7.2 covers the historic Multics system of
the 1960s (it was coming up at MIT when I was an undergraduate there). Multics
was complicated and revolutionary. Indeed, Thompson and Richie developed (and
named) Unix partially in rebellion to the complexity of Multics. Multics is no
longer used.

Section 3.7.3 covers the Intel Pentium _hardware_, which offers a segmentation
+demand-paging scheme that is not used by any of the current operating systems
(OS/2 used it in the past). The Pentium design permits one to convert the
system into a pure damand-paging scheme and that is the common usage today.

I will present the material in the following order.

  1. Describe segmentation+paging (not demand paging) generically, i.e. not tied to any specific hardware or software.
  2. Note the possibility of using demand paging (again generically).
  3. Give some details of the Multics implementation.
  4. Give some details of the Pentium hardware, especially how it can emulate straight demand paging.

#### ** Segmentation With (non-demand) Paging

![seg+page](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/seg+page.png)

One can combine segmentation and paging to get advantages of both at a cost in
complexity. In particular, user-visible, variable-size segments are the most
appropriate units for protection and sharing; the addition of (non-demand)
paging eliminates the placement question and external fragmentation (at the
smaller average cost of 1/2-page internal fragmentation per segment).

The basic idea is to employ (non-demand) paging on each segment. A
segmentation plus paging scheme has the following properties.

  * A virtual address becomes a triple: (seg#, page#, offset).
  * Each segment table entry (STE) points to the page table for that segment. Compare this with a  multilevel page table. 
  * The physical size of each segment is a multiple of the page size (since the segment consists of pages). The logical size is not; instead we keep the exact size in the STE (limit value) and terminate the process (or extend the size of the segment) if it references beyond the limit. In this case the last page of each segment is partially wasted (internal fragmentation).
  * The page# field in the address gives the entry in the chosen page table and the offset gives the offset in the page.
  * From the limit field, one can easily compute the size of the segment in pages (which equals the size of the corresponding page table in PTEs).
  * A straightforward implementation of segmentation with paging would requires 3 memory references (STE, PTE, referenced word) so a TLB is crucial.
  * Some books carelessly say that segments are of fixed size. This is wrong. They are of variable size with a fixed maximum and with the requirement that the physical size of a segment is a multiple of the page size.
  * Keep protection and sharing information on segments. This works well for a number of reasons. 
    1. A segment is variable size.
    2. Segments and their boundaries are user-visible,
    3. Segments are shared by sharing their page tables. This eliminates the problem mentioned above with shared pages.
  * Since we have paging, there is no placement question and no external fragmentation.
  * The problems are the complexity and the resulting 3 memory references for each user memory reference. The complexity is real. The three memory references would be fatal were it not for TLBs, which considerably ameliorate the problem. TLBs have high hit rates and for a TLB hit there is essentially no penalty. 

Although it is possible to combine segmentation with non-demand paging, I do
not know of any system that did this.

**Homework:** 46.  
When segmentation and paging are both being used, as in MULTICS, first the
segment descriptor must be looked up, then the page descriptor. Does the TLB
also work this way, with two levels of lookup?

**Homework:** Consider a 32-bit address machine using paging with 8KB pages and 4 byte PTEs. How many bits are used for the offset and what is the size of the largest page table? Repeat the question for 128KB pages. So far this question has been asked before. Repeat both parts assuming the system also has segmentation with at most 128 segments. Remind me to do this in class next time.

**Homework:** (Ask me about this one next class.) Consider a system with 36-bit addresses that employs both segmentation and paging. Assume each PTE and STE is 4-bytes in size.

  1. Assume the system has a page size of 8K and each process can have up to 256 segments. How large in bytes is the largest possible page table? How large in pages is the largest possible segment?
  2. Assume the system has a page size of 4K and each segment can have up to 1024 pages. What is the maximum number of segments a process can have? How large in bytes is the largest possible segment table? How large in bytes is the largest possible process.
  3. Assume the largest possible segment table is 213 bytes and the largest possible page table is 216 bytes. How large is a page? How large in bytes is the largest possible segment?

#### ** Segmentation With Demand Paging

There is very little to say. The previous section employed (non-demand) paging
on each segment. For the present scheme, we employ demand paging on each
segment, that is we perform fetch-on-demand for the pages of each segment.

#### The Multics Scheme

Multics was the first system to employ segmentation plus demand paging. The
implementation was as described above with just a few wrinkles, some of which
we discuss now together with some of the parameter values.

  * The Multics hardware (GE-645) was word addressable, with 36-bit words (the 645 predates bytes).
  * Each virtual address was 34-bits in length and was divided into three parts as mentioned above. The seg# field was the high-order 18 bits; the page# field was the next 6 bits; and the offset was the low-order 10 bits.
  * The actual implementation was more complicated and the full 34-bit virtual address was not present in one place in an instruction.
  * Thus the system supported up to 218=256K segments, each of size up to 26=64 pages. Each page is of size 210 (36-bit) words.
  * Since the segment table can have 256K STEs (called descriptors), the table itself can be large and was itself demand-paged.
  * Multics permits some segments to be demand-paged while other segments are not paged; a bit in each STE distinguishes the two cases.

#### The Pentium Scheme

The Pentium design implements a trifecta: Depending on the setting of a
various control bits the Pentium scheme can be pure demand-paging (current
OSes use this mode), pure segmentation, or segmentation with demand-paging.

The Pentium supports 214=16K segments, each of size up to 232 bytes.

  * This would seem to require a 14+32=46 bit virtual address, but that is not how the Pentium works. The segment number is _not_ part of the virtual address found in normal instructions.
  * Instead separate instructions are used to specify which are the currently active code segment and data segment (and other less important segments). Technically, the CS register is loaded with the selector of the active code segment and the DS register is loaded with the selector of the active data register.
  * When the selectors are loaded, the base and limit values are obtained from the corresponding STEs (called descriptors).
  * There are actually two flavors of segments, some are private to the process; others are system segments (including the OS itself), which are addressable (but not necessarily accessible) by all processes. 

Once the 32-bit segment base and the segment limit are determined, the 32-bit
address from the instruction itself is compared with the limit and, if valid,
is added to the base and the sum is called the 32-bit linear address. Now we
have three possibilities depending on whether the system is running in pure
segmentation, pure demand-paging, or segmentation plus demand-paging mode.

  1. In pure segmentation mode the linear address is treated as the physical address and memory is accessed.
  2. In segmentation plus demand-paging mode, the linear address is broken into three parts since the system implements 2-level-paging. That is, the high-order 10 bits are used to index into the 1st-level page table (called the page directory). The directory entry found points to a 2nd-level page table and the next 10 bits index that table (called the page table). The PTE referenced points to the frame containing the desired page and the lowest 12 bits of the linear address (the offset) finally point to the referenced word. If either the 2nd-level page table or the desired page are not resident, a page fault occurs and the page is made resident using the standard demand paging model.
  3. In pure demand-paging mode all the segment bases are zero and the limits are set to the maximum. Thus the 32-bit address in the instruction become the linear address without change (i.e., the segmentation part is effectively) disabled. Then the (2-level) demand paging procedure just described is applied.

Current operating systems for the Pentium use mode 3.

## 3.8 Research on Memory Management

Skipped

## 3.9 Summary

Read

## Some Last Words on Memory Management

We have studied the following concepts.

  * Segmentation / Paging / Demand Loading (fetch-on-demand). 
    * Each is a yes or no alternative.
    * This gives 8 possibilities.
  * Placement and Replacement.
  * Internal and External Fragmentation.
  * Page Size and locality of reference.
  * Multiprogramming level and medium term scheduling.

**Remark**: Do on the board the hw problem about sizes.

# Chapter 4 File Systems

There are three basic requirements for file systems.

  1. **Size**: Store very large amounts of data.
  2. **Persistence**: Data survives the creating process.
  3. **Concurrent Access**: Multiple processes can access the data concurrently.

High level solution: Store data in files that together form a file system.

## 4.1 Files

### 4.1.1 File Naming

Very important. A major function of the file system is to supply uniform
naming. As with files themselves, important characteristics of the file name
space are that it is persistent and concurrently accessible.

Unix-like operating systems extend the file name space to encompass devices as
well

Does each name refer to a unique file?  
Answer: Yes, providing the names start at the same place (absolute or relative
to the same directory).

Does each file have a unique name?  
Answer: Often no. We will discuss this below when we study links.

#### File Name Extensions

The extensions are suffixes attached to the file names and are intended to in
some way describe the high-level structure of the file's contents.

For example, consider the .html extension in class-notes.html, the name of the
file we are viewing. Depending on the system and application, these extensions
can have little or great significance. The extensions can be

  1. Conventions just for humans. For example letter.teq (my convention) signifies to me that this letter is written using the troff text-formatting language and employs the eqn preprocessor to handle mathematical equations and the tbl preprocessor to handle tables. Neither linux, troff, tbl, nor equ place any significance in the .teq extension.
  2. Conventions giving default behavior for some programs. 
    * The emacs editor by default edits .html files in html mode. However, emacs can edit such files in any mode and can edit any file in html mode. It just needs to be told to do so during the editing session.
    * The firefox browser assumes that an .html extension signifies that the file is written in the html markup language. However, having <html> ... </html> inside the file works as well.
    * The gzip file compressor/decompressor appends the .gz extension to files it compresses, but accepts a --suffix flag to specify another extension.
  3. Default behaviors for the operating system or window manager or desktop environment. 
    * Click on .xls file in windows and excel is started.
    * Click on .xls file in linux and libreoffice is started.
  4. _Required_ for certain programs. 
    * The gnu C compiler (and probably other C compilers) requires C programs be have the .c (or .h) extension, and requires assembler programs to have the .s extension.
  5. Required by the operating system 
    * MS-DOS treats .com files specially.

#### Case Sensitive?

Should file names be case sensitive. For example, do x.y, X.Y, x.Y all name
the same file? There is no clear answer.

  * Unix-like systems employ case sensitive file names so the three names given above are distinct.
  * Windows systems employ case insensitive file names so the three names given above are equivalent.
  * Mathematicians (and others) often "consider an element x of a set X" so use case sensitive naming.
  * Similarly, a Java programmer might say String string; (case sensitive). However an Ada programer would know that A:=a+1; is a simple increment (case insensitive).
  * Normal English (and other natural language) usage often employs case insensitivity (e.g. capitalizing a word at the beginning of a sentence does not change the word).

### 4.1.2 File Structure

How should the file be structured? Said another way, how does the OS interpret
the contents of a file.

A file can be interpreted as a

  1. Byte stream 
    * Unix, MacOS, windows.
    * Maximum flexibility.
    * Minimum structure.
    * All structure on a file is imposed by the applications that use it, not by the system itself.
  2. (fixed size-) Record stream: Out of date 
    * 80-character records for card images.
    * 133-character records for line printer files. Column 1 was for control (e.g., new page) Remaining 132 characters were printed.
  3. Varied and complicated beast. 
    * Indexed sequential.
    * B-trees.
    * Supports rapidly finding a record with a specific **key**.
    * Supports retrieving (varying size) records in key order.
    * Treated in depth in database courses.

### 4.1.3 File Types

The traditional file is simply a collection of data that forms the unit of
sharing for processes, even concurrent processes. These are called **regular
files**.

The advantages of uniform naming have encouraged the inclusion in the file
system of objects that are not simply collections of data.

#### Regular Files

  

##### Text vs Binary Files

Some regular files contain lines of text and are called (not surprisingly)
text files or ascii files (the latter name is of decreasing popularity as
latin-1 and unicode become more important). Each text line concludes with some
end of line indication: on unix and recent MacOS this is a newline (a.k.a line
feed), in MS-DOS it is the two character sequence carriage return followed by
newline, and in earlier MacOS it was carriage return.

Ascii, with only 7 bits per character, is poorly suited for most human
languages other than English. Latin-1 (8 bits) is a little better with support
for most Western European Languages.

Perhaps, with growing support for more varied character sets, ascii files will
be replaced by unicode (16 bits) files. The Java and Ada programming languages
(and perhaps others) already support unicode.

An advantage of all these formats is that they can be directly printed on a
terminal or printer.

Other regular files, often referred to as binary files, do not represent a
sequence of characters. For example, a four-byte, twos-complement
representation of integers in the range from roughly -2 billion to +2 billion
is definitely not to be thought of as 4 latin-1 characters, one per byte.

##### Application Imposed File Structure

Just because a file is unstructured (i.e., is a byte stream) from the OS
perspective does not mean that applications cannot impose structure on the
bytes. So a document written without any explicit formatting in MS word is not
simply a sequence of ascii (or latin-1 or unicode) characters.

On unix, an executable file must begin with one of certain magic numbers in
the first few bytes. For a native executable, the remainder of the file has a
well defined format.

Another option is for the magic number to be the ascii representation of the
two characters #! in which case the next several characters specify the
location of the executable program that is to be run with the current file fed
in as input. That is how some interpreted (as opposed to compiled) languages
work in unix.  
    #!/usr/bin/perl  
    perl script

#### Strongly Typed Files

In some systems the type of the file (which is often specified by the
extension) _determines_ what you can do with the file. This make the easy and
(hopefully) common case easier and, more importantly, safer.

It tends to make the unusual case harder. For example, you have a program that
turns out data (.dat) files. Now you want to use it to turn out a java file,
but the type of the output is data and cannot be easily converted to type java
and hence cannot be given to the java compiler.

#### Other-Than-Regular Files

We will discuss several file types that are not called regular.

  1. Directories.
  2. Symbolic Links, which are used to give alternate names to files.
  3. Special files (for devices). These use the naming power of files to unify many actions. 
    
              dir               # prints on screen
          dir > file        # result put in a file
          dir > /dev/audio  # results sent to speaker (sounds awful)
        

**Remark**: Lab4 (the last lab) assigned. It is due 10 December 2015.

### 4.1.4 File Access

There are two possibilities, sequential access and random access (a.k.a.
direct access).

With **sequential** access, each access to a given file starts where the
previous access to that file finished (the first access to the file starts at
the beginning of the file). Sequential access is the most common and gives the
highest performance. For some devices (e.g. magnetic or paper tape) access
must be sequential.

With **random** access, the bytes are accessed in any order. Thus each access
must specify which bytes are desired. This is done either by having each
read/write specify the starting location or by defining another system call
(often named seek) that specifies the starting location for the next
read/write.

For example, in unix, if no seek occurs between two read/write operations,
then the second begins where the first finished. That is, unix treats a
sequences of reads and writes as sequential, but supports seeking to achieve
random access.

Previously, files were declared to be sequential or random. Modern systems do
not do this. Instead all files are random, and optimizations are applied as
the system dynamically determines that a file is (probably) being accessed
sequentially.

### 4.1.5 File Attributes

Various properties that can be specified for a file For example:

  * hidden
  * do not backup
  * owner
  * key length (for keyed files)

### 4.1.6 File Operations

  * **Create**. The effect of create is essential if a system is to add files. However, it need not be a separate system call. (For example, it can be merged with open).
  * **Delete**. Essential, if a system is to delete files.
  * **Open**. Not essential. It is an optimization in which a process translates a file name to the corresponding disk locations only once per execution rather than once per access. We shall see that for the unix inode-based file systems, this translation can be quite expensive.
  * **Close**. Not essential. Frees resources without waiting for the process to terminate.
  * **Read**. Essential. Must specify filename, file location, number of bytes, and a buffer into which the data is to be placed. Several of these parameters can be set by other system calls and in many operating systems they are.
  * **Write**. Essential, if updates are to be supported. See read for parameters.
  * **Seek**. Not essential (could be in read/write). Specify the offset of the next (read or write) access to this file.
  * **Get attributes**. Essential if attributes are to be used.
  * **Set attributes**. Essential if attributes are to be user settable.
  * **Rename**. Copy and delete is not an acceptable substitute for big files. Moreover, copy-delete is not atomic. Indeed link-delete is not atomic so, even if link (discussed below) is provided, renaming a file adds functionality.

**Homework:** 4\. Is the open system call in UNIX absolutely essential? What would be the consequences of not having it?

**Homework:** 5\. Systems that support sequential files always have an operation to rewind files. Do systems that support random-access files need this, too?

**Homework:** 6\. Some operating systems provide a system call RENAME to give a file a new name. Is there any difference at all between using the call to rename a file and just copying the file to a new file with the new name, followed by deleting the old one? 

### 4.1.7 An Example Program Using File System Calls

Let's look at [copyfile.c](diagrams/copyfile.c.pdf) to see the use of file
descriptors and error checks, even though there could be more attention to
errors.

Note specifically, the code checks the return value from each I/O system call.
It is a common error to assume that

  1. Open always succeeds. It can fail due to the file not existing or the process having inadequate permissions.
  2. Read always succeeds. An end of file can occur. Fewer than expected bytes could have been read. Also the file descriptor could be bad, but this should have been caught when checking the return value from open.
  3. Create always succeeds. It can fail when the disk (partition) is full, or when the process has inadequate permissions.
  4. Write always succeeds. It too can fail when the disk is full or the process has inadequate permissions.

## 4.2 Directories

Directories form the primary unit of organization for the filesystem.

### 4.2.1-4.2.3 Single-Level (Two-Level) and Hierarchical Directory Systems

![dir sys levels](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/dir-sys-
levels.png)

One often refers to the level structure of a directory system. It is easy to
be fooled by the names given. A single level directory structure results in a
file system tree with **two** levels: the single root directory and (all) the
files in this directory. That is, there is one level of directories and
another level of files so the full file system tree has two levels.

Possibilities.

  * One directory in the system (single-level). This possibility is illustrated by the top left tree.
  * One directory per user and a root above these (two-level). This possibility is illustrated by the top right tree.
  * One tree in the system. This possibility is illustrated by the bottom tree.
  * One tree per user with a root above. This possibility is also illustrated by the bottom tree.
  * One forest in the system. This possibility is illustrated by viewing all three trees as together constituting the file system forest.
  * One forest per user. This possibility is illustrated by viewing the top two trees as belong to one user and the bottom tree as belonging to a second user (a tree is a special case of a forest).

These possibilities are not as wildly different as they sound or as the
pictures suggests.

  * Assume the system has only one directory, but also assume the character / is allowed in a file name. Then one could fake a tree by having a file named  
/allan/gottlieb/courses/os/class-notes.html  
rather than a directory allan, a subdirectory gottlieb, ..., a file class-
notes.html.

  * The Dos (windows) file system is a forest, the Unix file system is a tree (until we learn about links below, then it is not even a forest). In Dos, there is no common parent of a:\ and c:\, so the file system is not a tree. But Windows explorer makes the dos forest look quite a bit like a tree.
  * You can get an effect similar to one X per user by having just one X in the system and having permissions that permits each user to visit only a subset. Of course if the system doesn't have permissions, this is not possible.
  * Today's multiuser systems have a tree per system or a forest per system. This is not strictly true due to links, which we will study soon.
  * Simple embedded systems often use a one-level directory system. 

### 4.2.4 Path Names

You can specify the location of a file in the file hierarchy by using either
an **absolute** or a **relative** path to the file.

  * An absolute path starts at the (or one of the, if we have a forest) root(s).
  * A relative path starts at the **current** (a.k.a working) directory. In order to support relative paths, a process must know its current directory and there must be such a field in the process control block.
  * The special directories . and .. represent the current directory and the parent of the current directory respectively. In the (or a) root .. and . both represent the current (root) directory.

**Homework:** Give 8 different path names for the file /etc/passwd.

**Homework:** 8\. A simple operating system supports only a single directory but allows it to have arbitrarily many files with arbitrarily long file names. Can something approximating a hierarchical file system be simulated? How?.

### 4.2.5 Directory Operations

Remember that the job of a director is to map names (of its children) to the
files represented by the those names.

  1. **Create**. Produces an empty directory. Normally the directory created actually contains . and .., so is not really empty
  2. **Delete**. The delete system call requires the directory to be empty (i.e., to contain just . and ..). Delete commands intended for users have options that cause the command to first empty the directory (except for . and ..) and then delete it. These user commands make use of both file and directory delete system calls.
  3. **Opendir**. As with the file open system call, opendir creates a handle for the directory that speeds future access by eliminating the need to process the name of the directory.
  4. **Closedir**. As with the file close system call, closedir is an optimization that enables the system to free resources prior to process termination.
  5. **Readdir**. In the old days (of unix) one could read directories as files so there was no special readdir (or opendir/closedir) system call. It was then believed that the uniform treatment would make programming (or at least system understanding) easier as there was less to learn.  
However, experience has taught that this was a poor idea since the structure
of directories was exposed to users. Early unix had a simple directory
structure and there was only one type of structure for all implementations.
Modern systems have more sophisticated structures and more importantly they
are not fixed across implementations. So if programs used read() to read
directories, the programs would have to be changed whenever the structure of a
directory changed. Now we have a readdir() system call that knows the
structure of directories. Therefore if the structure is changed only readdir()
need be changed.  
This is an example of the software principle of information hiding.

  6. **Rename**. Similar to the file rename system call. Again note that rename is atomic; whereas, creating a new directory, moving the contents, and then removing the old one is not.
  7. **Link**. Add another name for a file; discussed below.
  8. **Unlink**. Remove a directory entry. This is how a file is deleted. However, if there are many links and just one is unlinked, the file remains. Unlink is discussed in more detail below.
  9. There is **no** Writedir operation. Directories are written as a side effect of other operations.

### 4.2.A Mounting One Filesystem on Another (Unix)

I have mentioned that in Unix all files can be accessed from the single root.
This does not seem possible when you have two disks (or two partitions on one
disk, which is nearly the same thing). How can you get from the root of one
partition to anywhere in the other?

![mount](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/mount.png)

One solution might be to make a super-root having the two original roots as
children. However, this is not done. Instead, one of the devices is _mounted_
on the other, as is illustrated in the figures on the right.

The top row shows two filesystems (on separate devices). From either root, you
can easily get to all the files in that filesystem. Filesystems on Windows
machines leave the situation as shown and have syntax to change our focus from
one filesystem to another.

Unix uses a different approach. In the normal case (the only one we will
consider), one **mount**s one filesystem on an empty directory of the other.
For example, the bottom row shows the result of mounting the right filesystem
on the directory /y of the left filesystem.

In this way, the forest of the top row becomes a tree in the bottom. However,
we shall see below that the introduction of (hard and symbolic) links in Unix
results in filesystems that are not trees. It is true however, that you can
name any file starting from the (single) root.

## 4.3 File System Implementation

Now that we understand how the file system looks to a user, we turn our
attention to how it is implemented.

### 4.3.1 File System Layout

We look at how the file systems are laid out on disk in modern PCs. Much of
this is required by the bios so all PC operating systems have the same lowest
level layout. I do not know the corresponding layout for mainframe systems or
supercomputers.

A system often has more than one physical disk. The first disk is the boot
disk. How do we determine which is the first disk?

  1. Easiest case: only one disk.
  2. Only one disk controller. The disk with the lowest number is the boot disk. The numbering is system dependent, for SCSI (small computer system interconnect, now used on big computers as well) you set switches on the drive itself.
  3. Multiple disk controllers. The controllers are ordered in a system dependent way.

The BIOS reads the first sector (smallest addressable unit of a disk) of the
boot disk into memory and transfers control to it. A sector contains 512
bytes. The contents of this particular sector is called the MBR (master boot
record).

The MBR contains two key components: the partition table and the first-level
loader.

  * A disk can be logically divided into variable size **partitions**, each acting as a logical disk. That is, normally each partition holds a complete file system. The partition table (like a process's page table) gives the starting point of each partition. It is actually more like the segment table of a pure segmentation system since the objects pointed to (partitions and segments) are of variable size. As with segments, the size of each partition is stored in the corresponding entry of the partition table.
  * One partition in the partition table is marked as the active partition.
  * The first level loader then loads 2nd-level loader, which resides in the first sector of the active partition, and transfers control to it. This sector is called the boot sector or boot block.
  * The boot block then loads the OS (actually it can load another loader, etc) 

#### Contents of a Partition (Containing a Filesystem)

The contents of a filesystem vary from one file system to another but there is
some commonality.

  * Each partition has a boot block as mentioned above.
  * Most partitions contain one filesystem.
  * Each such partition must have some information saying what type of file system it contains. The region containing this and other administrative information is often called the superblock. The location of the superblock is fixed.
  * The root directory is either stored in a fixed location, or its location is in a fixed position in the superblock, or (as in unix i-node file systems) the root i-node is in a fixed location (or it is pointed to from a fixed location in the superblock). The root i-node points to the root directory. We will have more to say about i-nodes below.
  * A list of free (i.e., available) disk blocks must be maintained. If these blocks are linked together, the head of the list (or a pointer to it) must be in a well defined spot. If a bitmap is used, it (or a pointer to it) must be in a well defined place.
  * Files and directories (i.e., in use disk blocks). These are of course the reason we have the file system.
  * For i-node based systems, the i-nodes are normally stored in a separate region of the partition.

### 4.3.2 Implementing Files

A fundamental property of disks is that they cannot read or write single
bytes. The smallest unit that can be read or written is called a **sector**
and is normally 512 bytes (plus error correction/detection bytes). This is a
property of the hardware, not the operating system.  Recently some drives have
much bigger sectors, but we will ignore this fact.

The operating system reads or writes disk **blocks**. The size of a block is a
multiple (normally a power of 2) of the size of a sector. Since sectors are
(for us) always 512 bytes, the block size can be 512, 1024=1K, 2K, 4K, 8K,
16K, etc. The most common block sizes today are 4K and 8K.

So files will be composed of blocks.

When we studied memory management, we had to worry about fragmentation,
processes growing and shrinking, compaction, etc. Many of these same
considerations apply to files; the difference (largely in nominclature) is
that instead of a memory region being composed of bytes, a file is composed of
blocks.

#### Contiguous Allocation

Recall the simplest form of memory management beyond uniprogramming was OS/MFT
where memory was divided into a very few regions and each process was given
one of these regions. The analogue for disks would be to give each file an
entire partition. This is too inflexible and is not used for files.

The next simplest memory management scheme was the one used in OS/MVT (a
swapping system), where the memory for a process was contiguous.

  * The analogous scheme for files is called contiguous allocation.
  * Each file is stored as one piece.
  * This scheme is simple and fast for access since, as we shall see next chapter, disks give much better performance when accessed sequentially.
  * However contiguous allocation is problematic for growing files. 
    * If a growing file reaches another file, the system must move files.
    * The extreme would be to compactify the disk, which entails moving many files and the resulting configuration with no holes will have trouble with any file growing (except the last file).
    * OS/MVT had the analogous problem when jobs grew.
  * As with memory, there is the problem of external fragmentation.
  * Contiguous allocation is no longer used for general purpose rewritable file systems.
  * It is ideal for file systems where files do not change size.
  * It is used for CD-ROM file systems.
  * It is used (almost) for DVD file systems. A DVD movie is a few gigabytes in size but the 30 bit file length field limits files to 1 gigabyte so each movie is composed of a few contiguous files. The reason I said almost is that the terminology used is that the movie is one file stored as a sequence of **extents** and only the extents are contiguous. 

**Homework:** 11\. (There is a typo: the first sentence should end at the first comma.) Contiguous allocation of files leads to disk fragmentation. Is this internal fragmentation or external fragmentation? Make an analogy with something discussed in the previous chapter. 

#### Linked Allocation

A file is an ordered sequence of blocks. We just considered storing the blocks
one right after the other (contiguous) the same way that one can store an in-
memory list as an array. The other common method for in-memory lists is to
link the elements together via pointers. This can also be done for files as
follows.

  * The directory entry for the file contains a pointer to the first block of the file.
  * Each block of a file contains a pointer to the next block the file.

However, this scheme gives horrible performance for random access: N disk
accesses are needed to access block N.

As a result _this implementation_ of linked allocation is not used.

Consider the following two code segments that store the same data but in a
different order. The first is analogous to the horrible linked list file
organization above and the second is analogous to the ms-dos FAT file system
we study next.

    
    
      struct node_type {
          float data;                  float node_data[100];
          int   next;                  int   node_next[100];
      } node[100]
    

With the second arrangement the data can be stored far away from the next
pointers. In FAT this idea is taken to an extreme: The data, which is large (a
disk block), is stored on disk; whereas, the next pointers, which are small
(each is an integer) are stored in memory in a File Allocation Table or FAT.
(When the system is shut down the FAT is copied to disk and when the system is
booted, the FAT is copied to memory.)

#### The FAT (File Allocation Table) File System

The FAT file system stores each file as a linked list of disk blocks. The
blocks, which contain file data only (not the linked list structure) are
stored on disk. The pointers implementing the linked list are stored in
memory.

![ms-dos](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/ms-dos.png)

  * There is a long lineage of FAT file systems (FAT-12, FAT-16, vfat, ...) all of which use the file allocation table. The following description of FAT is fairly generic and applies to all of them.
  * FAT was the file system used by dos and and early versions of Windows.
  * The NT series of Windows (NT, 2000, XP, Vista, 7, 8) supports FAT as well as the superior NTFS (NT File System).
  * Linux has full support for FAT (and improving support for NTFS).
  * MacOS has full support for FAT.
  * FAT is used on flash RAMS (USB memory sticks) as well as memory cards for digital cameras.
  * The directory entry for a file points to the first block (i.e., the directory entry specifies the block number).
  * The FAT itself (i.e., the table) is maintained in memory having one (1-word) entry for each disk block. The entry for block N contains the block number of the next block in the same file as N. If block N is the last block of a file, the entry is EOF. An example FAT is on the right. The directory entry for file A contains 4, the entry for B contains 6. Let's trace the steps to find all the blocks in each file.
  * FAT implements linked allocation but the links are stored separate from the data.
  * The time needed to access a random block is still is linear in the size of the file but now all the references are to the FAT, which is in memory. So it is bad for random accesses, but not nearly as horrible as plain linked allocation.
  * The size of the table is one pointer per disk block. So the ratio of the disk space supported to the memory space needed is 
    
              (size of a disk block) / (size of a pointer)
        

If the block size is 8KB and a pointer is 2B, the memory requirement is 1/4
megabyte for each disk gigabyte. Large but not prohibitive. (While 8KB is
reasonable today for blocksize, 2B pointers is not since that would mean the
largest partition could be 216 blocks = 216×213 bytes = 229 bytes = 1/2 GB,
which is much too small.)

  * If the block size is 512B (the sector size of most disks) and a pointer is 8B then the memory requirement is 16 megabytes for each disk gigabyte, which would most likely be prohibitive. 

More details can be found in [ this lecture
](http://www.c-jump.com/CIS24/Slides/FAT/lecture.html) from Igor Kholodov. (A
local copy is [here).](kholodov-fat.html)

#### The Unix Inode-based Filesystem

![inodes](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/inodes.png)

Continuing the idea of adapting storage schemes from other regimes to file
storage, why don't we mimic the idea of (non-demand) paging and have a table
giving, for each block of the file, where on the disk that file block is
stored? In other words a ``file block table'' mapping each file block to its
corresponding disk block. This is the idea of (the first part of) the unix
i-node solution, which we study next.

Although Linux and other Unix and Unix-like operating systems have a variety
of file systems, the most widely used Unix file systems are i-node based as
was the original Unix file system from Bell Labs. As we shall see i-node file
systems are more complicated than straight paging, they have aspects of
multilevel paging as well.

There is some question of what the i stands for. The consensus seems to be
index. Now, however, people often write inode (not i-node) and don't view the
i as standing for anything. For example Dennis Richie doesn't remember why the
name was chosen (lkml.indiana.edu/hypermail/linux/kernel/0207.2/1182.html).

> In truth, I don't know either. It was just a term that we started to use.
"Index" is my best guess, because of the slightly unusual file system
structure that stored the access information of files as a flat array on the
disk, with all the hierarchical directory information living aside from this.
Thus the i-number is an index in this array, the i-node is the selected
element of the array. (The "i-" notation was used in the 1st edition manual;
its hyphen became gradually dropped).

Inode based systems have the following properties.

  1. Each file and directory has an associated inode, which enables the system to find the blocks of the file or directory.
  2. The inode associated with the root (called the root inode) is at a known location on the disk. In particular, the root inode can be found by the system.
  3. The directory entry for a file contains a pointer to the file's i-node.
  4. The directory entry for a subdirectory contains a pointer to the subdirectory's i-node.
  5. The metadata for a file or directory is stored in the corresponding inode.
  6. The inode itself points to the first few data blocks, often called direct blocks. I believe in early systems there were 10 direct blocks pointers in each inode. In the diagram, the inode contains pointers to six direct blocks, and all data blocks are colored blue.
  7. The inode also points to an indirect block, which then points to a number K of disk blocks. K=(blocksize)/(pointersize). In the diagram, the indirect blocks (technically single indirect blocks) are colored green.
  8. The inode also points to a double indirect block, which points to a K single indirect blocks, each of which points to K data blocks. In the diagram, double indirect blocks are colored magenta.
  9. For some implementations there is a triple indirect block as well. A triple indirect block points to K double indirect blocks, which point ... . In the diagram, the triple indirect block is colored yellow.
  10. The i-node is in memory for open files. So references to direct blocks require just one I/O.
  11. For big files most references require two I/Os (indirect + data).
  12. For huge files most references require three I/Os (double indirect, indirect, and data).
  13. For humongous files most references require four I/Os.
  14. Actually, fewer I/Os are normally required due to caching.
  

##### Retrieving a Block in an Inode-Based File System

Given a block number (byte number / block size), how do you find the block?
Specifically, if we assume

  1. The file system does not have a triple indirect block.
  2. We desire block number _N_, where _N=0_ is the first block.
  3. There are _D_ direct pointers in the inode. These pointers are numbered _0..(D-1)_.
  4. There are K pointers in each indirect block. These pointers are numbered _0..(K-1)_.

then the following algorithm can be used to find block _N_.

    
    
      If N < D           // This is a direct block in the i-node
        use direct pointer N in the i-node
      else if N < D + K  // The single indirect block has a pointer to this block
        use pointer D in the inode to get the indirect block
        then use pointer N-D in the indirect block to get block N
      else   // This is one of the K*K blocks obtained via the double indirect block
        use pointer D+1 in the inode to get the double indirect block
        let P = (N-(D+K)) DIV K      // Which single indirect block to use
        use pointer P to get the indirect block B
        let Q = (N-(D+K)) MOD K      // Which pointer in B to use
        use pointer Q in B to get block N
    

For example, let D=12, assume all blocks are 1000B, assume all pointers are
4B. Retrieve the block containing byte 1,000,000.

  * K = 1000/4 = 250.
  * Byte 1,000,000 is in block number N=1000.
  * N > D + K so we need the double indirect block.
  * Follow pointer number D+1=13 in the inode to retrieve the double indirect block.
  * P=(1000-(12+250)) DIV 250 = 738 DIV 250 = 2.
  * Follow pointer number P=2 in the double indirect block to retrieve the needed single indirect block.
  * Q=(1000-(12+250)) MOD 250 = 738 MOD 250 = 238.
  * Follow pointer number 238 in the single indirect block to retrieve the desired block (block number 1000). 

With a triple indirect block, the ideas are the same, but there is more work.

**Homework:** Consider an inode-based system with the same parameters as just above, D=12, K=250, etc.

  1. What is the largest file that can be stored.
  2. How much space is used to store this largest possible file assuming the attributes require 64B?
  3. What percentage of the space used actually holds file data?
  4. Repeat all the above, now assuming the file system supports a triple indirect block.
  5. Remind me to do this one in class next time.

### 4.3.3 Implementing Directories

Recall that the primary function of a directory is to map the file name (in
ASCII, Unicode, or some other text-based encoding) to whatever is needed to
retrieve the data of the file itself.

There are several ways to do this depending on how files are stored.

  * For contiguously allocated files, the directory entry for a file contains the starting address on the disk and the file size. Since disks can only be accessed by sectors, we store the sector number. The system can choose to start all files on a block (rather than sector) boundary in which case the block number, which is smaller, is stored instead.
  * For linked allocation (pure linked or FAT-based) the directory entry again points to the first block of the file.
  * For inode-based file systems, the directory entry points to the inode. 

Another important function is to enable the retrieval of the various
attributes (e.g., length, owner, size, permissions, etc.) associated with a
given file.

  * One possibility is to store the attributes in the directory entry for the file. Windows does this.
  * Another possibility for inode-based systems, is to store the attributes in the inode as we have suggested above. The inode-based file systems for Unix-like operating systems do this.

**Homework:** 30 It has been suggest that the first part of each Unix file be kept in the same disk block as its i-node. What good would this do?

#### Long File Names

It is convenient to view the directory as an array of entries, one per file.
This view tacitly assumes that all entries are the same size and, in early
operating systems, they were. Most of the contents of a directory are
inherently of a fixed size. The primary exception is the file name.

Early systems placed a severe limit on the maximum length of a file name and
allocated this much space for all names. DOS used an 8+3 naming scheme (8
characters before the dot and 3 after). Unix version 7 limited names to 14
characters.

Later systems raised the limit considerably (255, 1023, etc) and thus
allocating the maximum amount for each entry was inefficient and other schemes
were used. Since we are storing variable size quantities, a number of the
consideration that we saw for non-paged memory management arise here as well.

#### Searching Directories for a File

The simple scheme is to search the list of directory entries linearly, when
looking for an entry with a specific file name. This scheme becomes
inefficient for very large directories containing hundreds or thousands of
files. In this situation a more sophisticated technique (such as hashing or
B-trees) is used.

### 4.3.4 Shared (Multinamed) Files (Links)

We often think of the files and directories in a file system as forming a tree
(or forest). However in most modern systems this is not necessarily the case,
the same file can appear in two (or more) different directories (not two
copies of the file, but the _same_ file). It can also appear multiple times in
the same directory, having different names each time.

I like to say that the same file has two different names. One can also think
of the file as being shared by the two directories (but those words don't work
so well for a file with two names in the same directory).

  * Shared files is Tanenbaum's terminology.
  * If a file exists, one can create another name for it (quite possibly in another directory).
  * This is often called creating another link to the file.
  * Unix has two flavor of links, **hard links** and **symbolic links** (a.k.a. **symlinks**).
  * Dos/windows has shortcuts, which behave somewhat like symlinks, but I don't believe it has an analogue of hard links.
  * We will concentrate on both flavors of unix links.
  * These links often cause confusion, but I really believe that the diagrams I created make it all clear. 

#### Hard Links

With unix hard links there are multiple names for the same file and each name
has **equal status**. The directory entries for both names point to the
**same** inode.

  * Hard links are thus _symmetric_ multinamed files.
  * When a hard link is created _another_ name is created for the _same_ file. The number of files in the system is _the same_ before and after the hard link is created.
  * In the i-node implementation of Unix file systems, creating a hard link does _not_, repeat **NOT** create a new i-node.
  * It is _not_, I repeat **NOT**, true that one name is the real name and the other one is just a link.
  * Indeed, after the hard link has been created it is not possible to tell which was the original name and which is the newly created link. 
![dir-tree](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/dir-tree.png)

For example, the diagram on the right illustrates the result that occurs when,
starting with an empty file system (i.e., just the root directory) one
executes

    
    
      cd /
      mkdir /A; mkdir /B
      touch /A/X; touch /B/Y
    

The diagrams in this section use the following conventions

  * Yellow circles represent ordinary files.
  * Blue squares represent directories.
  * Names are written on the edges. For example, one name for the left circle is /A/X. 
    * It is not customary to write the names on the edges, normally they are written in the circles and squares.
    * When there are no multi-named files, it doesn't matter if they are written in the node or on the edge.
    * We will see that when files can have multiple names it is much better to write the name on the edge. 
![hard-link](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/hard-link.png)

Now we execute ` ln /B/Y /A/New ` which leads to the next diagram on the
right.

Note that there are still exactly 5 inodes and 5 files: two regular files and
three directories. All that has changed is that there is another name for one
of the regular files. At this point there are two equally valid name for the
right hand yellow file, /B/Y and /A/New. The fact that /B/Y was created first
is **NOT** detectable.

  * The directory entries for both file names point to the **same** i-node.
  * The file has only one owner (the one who created the file initially).
  * The file has one date of last access (the last access by any of its names), one set of permissions, one ... .
  * Note the usage: the file nameS (plural) vs the file (singular).
  * Note also that when creating a hard link the existing file must be an ordinary file and **not** a directory. In particular, we could not have said 
    
              ln /B /A/NewDir
        

![hard-link-2](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/hard-
link-2.png)

Next assume Bob created /B and /B/Y and Alice created /A, /A/X, and /A/New.
Later Bob tires of /B/Y and removes it by executing

    
    
      rm /B/Y
    

The file /A/New is still fine (see the diagram on the right). But it is owned
by Bob, who can't find it! If the system enforces quotas Bob will likely be
charged (as the owner), but he can neither find nor delete the file (since Bob
cannot unlink, i.e. remove, files from /A).

If, prior to removing /B/Y, Bob had examined its link count (an attribute of
the file), he would have noticed that there is another (hard) link to the
file, but would not have been able to determine in which directory (/A in this
case) the hard link was located or what is the name of the file in that
directory (New in this case).

Since hard links are only permitted to files (not directories) the resulting
file system is a dag (directed acyclic graph). That is, there are no directed
cycles. We will now proceed to give away this useful property by studying
symlinks, which _can_ point to directories.

#### Symlinks

As just noted, hard links do **NOT** create a new file, just another name for
an existing file. Once the hard link is created the two names have equal
status.

Symlinks, on the other hand **DO** create another file, a non-regular file,
that itself serves as another name for the original file. Specifically

  * Creation of a symlink results in an _asymmetric_ multi-named file. Assuming the original was a regular file, the symlink does indeed have a different status.
  * When a symlink is created **another** file is created. The **contents** of the new file is the **name** of the original file.
  * A hard link in contrast **is** (another name for) the original file.
  * The examples should make this clear.

Again start with an empty file system and this time execute the following code
sequence (the only difference from the above is the addition of a -s).

    
    
      cd /
      mkdir /A; mkdir /B
      touch /A/X; touch /B/Y
      ln -s /B/Y /A/New
    

![symlink](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/symlink.png)

We now have an additional file /A/New, which is a symlink to /B/Y.

  * The additional file entails an additional inode. The diagram on the right shows 3 directories, 2 regular files, and 1 symlink. This count implies 3+2+1=6 inodes (assuming an i-node based file system).
  * The file named /A/New has the string /B/Y as its _data_ (_not_ metadata).
  * The system notices that /A/New is a red diamond (a symlink, **not** a regular file) so reading /A/New will return the contents of /B/Y (assuming the reader has read permission for /B/Y).
  * It is also possible to read the contents of /A/New itself (those contents are the four characters /B/Y).
  * The _size_ of A/New is 4 bytes, one byte per character '/', 'B', '/', and 'Y'.
  * If /B/Y is removed, /A/New becomes invalid.
  * If a new /B/Y is created, /A/New is once again valid.
  * Removing /A/New has no effect of /B/Y.
  * Examining /B/Y does not reveal the existence of /A/New.
  * If a user has write permission for /B/Y, then writing /A/New is possible and writes /B/Y.

The bottom line is that, with a hard link, a new **name** is created for the
file. This new name has equal status with the original name. This can cause
some surprises (e.g., _you_ create a link but _I_ own the file). With a
symbolic link a new **file** is created (owned by the creator naturally) that
contains the name of the original file. We often say the new file points to
the original file.

**Question**: Consider the hard link setup above. If Bob removes /B/Y and then creates another /B/Y, what happens to /A/New?  
**Answer**: Nothing. /A/New is still a file owned by **Bob** having the same contents, creation time, etc. as the _original_ /B/Y.

**Question**: What about with a symlink?  
**Answer**: /A/New becomes invalid and then valid again, this time pointing to the _new_ /B/Y. (It can't point to the old /B/Y as that is completely gone.)

**Note:**  
Shortcuts in windows contain more than symlinks contain in unix. In addition
to the file name of the original file, they can contain arguments to pass to
the file if it is executable. So ashortcut to firefox.exe can specify
firefox.exe //cs.nyu.edu/~gottlieb/courses/os/class-notes.html

Moreover, as was pointed out by students in my 2006-07 fall class, the
shortcuts are not a feature of the windows FAT file system itself, but simply
the actions of the command interpreter when encountering a file named *.lnk  
**End of Note**.

##### Symlinking a Directory

![simlink-dir](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/symlink-
dir.png)

What happens if the target of the symlink is an existing directory? For
example, consider the code below (again starting with an empty file system),
which gives rise to the diagram on the right.

    
    
      cd /
      mkdir /A; mkdir /B
      touch /A/X; touch /B/Y
      ln -s /B /A/New
    

Some questions

  * Is there a file named /A/New/Y ?  
Answer: Yes.

  * What happens if you execute cd /A/New; dir ?  
Answer: You see a listing of the files in /B, in this case the single file Y.

  * What happens if you execute cd /A/New/.. ?  
Answer: Not clear!  
Clearly you are changing the current working directory to the parent directory
of /A/New. But is that /A or /?  
The command interpreter I use offers both possibilities.

    * cd -L /A/New/.. takes you to A (L for logical).
    * cd -P /A/New/.. takes you to / (P for physical).
    * cd /A/New/.. takes you to A (logical is the default).
  * What did I mean when I said the pictures made it all clear?  
Answer: From the file system perspective it is clear. It is not always so
clear what programs will do.

### 4.3.5 Log-Structured File Systems

This research project of the early 1990s was inspired by the key observation
that systems are becoming limited in speed by small writes. The factors
contributing to this phenomenon were (and still are).

  1. The CPU speed increases have far surpassed the disk speed increases so the system has become I/O limited.
  2. The large buffer cache found on modern systems has led to fewer read requests actually requiring I/Os.
  3. A disk I/O requires almost 10ms of preparation before any data is transferred, and then can transfer a block in less than 1ms. Thus, a one block transfer spends most of its time getting ready to transfer.

The goal of the log-structured file system project was to design a file system
in which all writes are large and sequential (most of the preparation is
eliminated when writes are sequential). These writes can be thought of as
being appended to a log, which gave the project its name.

  * The project worked with a unix-like file system, i.e. it was i-node based.
  * The system accumulates writes in a buffer until have (say) 1MB to write.
  * When the buffer is full, write it to the end of the disk (treating the disk as a log).
  * Thus writes are sequential and large and hence fast.
  * When any part of a file is changed, the i-node is rewritten.
  * The 1MB units on the disk are called (unfortunately) segments. I will refer to the buffer as the segment buffer.
  * A segment can contain i-nodes, direct blocks, indirect blocks, blocks forming part of a file, and blocks forming part of a directory. In short a segment contains the most recently modified (or created) 1MB of blocks.
  * Note that the now useless overwritten blocks are not reclaimed!
  * The system keeps a map of where the most recent version of each i-node is located. This map is on disk (but the heavily accessed parts will be in the buffer cache).
  * So the (most up to date) i-node of a file can be found and from that the entire file can be found.
  * But the disk will fill with garbage since modified blocks are not reclaimed.
  * A cleaner process runs in the background and examines segments starting from the beginning. It removes overwritten blocks and then adds the remaining blocks to the segment buffer. (This is very much not trivial.)
  * Thus the disk is compacted and is treated like a circular array of segments. 

Despite the advantages given, log-structured file systems have not caught on.
They are incompatible with existing file systems and the cleaner has proved to
be difficult.

### 4.3.6 Journaling File Systems

Many seemingly simple I/O operations are actually composed of sub-actions. For
example, deleting a file on an i-node based system (really this means deleting
the last link to the i-node) requires removing the entry from the directory,
placing the i-node on the free list, and placing the file blocks on the free
list.

What happens if the system crashes during a delete and some, but not all
three, of the above actions occur?

  * If the operations are guaranteed to be done in the order given, then the worst that can occur is that the entry is removed from the directory, but some file blocks and possibly the i-node are not reclaimed. This wastes resources, but is not a disaster.
  * As we will learn later, I/O performance is sometimes improved if operations are executed out of order.
  * In that case we can have a directory entry pointing to an i-node that has been freed or an i-node referring to blocks that have been freed.
  * Since free blocks and i-nodes are later reassigned to other files, the results can be catastrophic.

A journaling file system prevents these problems by using an idea from
database theory, namely transaction logs. To ensure that the multiple sub-
actions are all performed, the larger I/O operation (delete in the example) is
broken into 3 steps.

  1. Write a log entry stating what has to be done and ensure it is written to disk.
  2. Start doing the sub-actions.
  3. When all sub-actions complete, mark the log entry as complete (and eventually erase it)..

After a crash, the log (called a journal) is examined and if there are pending
sub-actions, they are done before the system is made available to users.

Since sub-actions may be repeated (once before the crash, and once after), it
is required that they all be _idempotent_ (applying the action twice is the
same as applying it once).

Some history.

  * IBM's AIX had a journaling file system in 1990.
  * NTFS had journaling from day 1 (1993).
  * Many Unix systems have it now.
  * The main linux file system (ext2) added journaling (and became ext3, then ext4) in 2001. Journaling appeared earlier that year in other Linux file systems.
  * Journaling was added to HFS+, the MacOS file system, in 2002.
  * FAT has never had journaling (and probably never will).

### 4.3.7 Virtual File Systems

![vfs](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/vfs.png)

A single operating system needs to support a variety of file systems. The
software support for each file system would have to handle the various I/O
system calls defined.

Not surprisingly the various file systems often have a great deal in common
and large parts of the implementations would be essentially the same. Thus for
software engineering reasons one would like to abstract out the common part.

This was done by Sun Microsystems when they introduced NFS the Network File
System for Unix and by now most unix-like operating systems have adopted this
idea. The common code is called the VFS layer and is illustrated on the right.

The original motivation for Sun was to support NFS (Network File System),
which permits a file system residing on machine A to be mounted onto a file
system residing on machine B. The result is that by cd'ing to the appropriate
directory on machine B, a user with sufficient privileges can
read/write/execute the files in the machine A file system.

Note that mounting one file system onto another (whether they are on different
machines or not) does **not** require that the two file systems be the same
type. For example, I routinely mount FAT file systems (from MP3 players,
cameras, ets) on to my Linux inode-based file system. The involvement of
multiple file system software components for a single operation is another
point in VFS's favor.

Nonetheless, I consider the idea of VFS to be mainly good (perhaps superb)
software engineering more than OS design. The details are naturally OS
specific.

## 4.4 File System Management and Optimization

Since I/O operations can dominate the time required for complete user
processes, considerable effort has been expended to improve the performance of
these operations.

### 4.4.1 Disk Space Management

All general purpose file systems use a paging-like algorithm for file storage
(read-only systems, which often use contiguous allocation, are the major
exception). Files are broken into fixed size pieces, called **blocks** that
are scattered over the disk.

Note that although this algorithm is similar to paging, it is _not_ called
paging and often does not have an explicit page table.

Note also that all the blocks of the file are present at all times, i.e., this
system is **not** _demand_ paging.

One can imagine systems that do utilize demand-paging-like algorithms for disk
block storage. In such a system only some of the file blocks would be stored
on disk with the rest on tertiary storage (some kind of tape, or holographic
storage perhaps). NASA might do this with their huge datasets.

#### Choice of Block Size

We discussed a similar question before when studying page size. The sizes
chosen are similar, both blocks and pages are measured in kilobytes. Common
choices are 4KB and 8KB, for each.

There are two conflicting goals, performance and efficient memory
utilization..

  1. We will learn next chapter that large disk transfers achieve much higher total bandwidth than small transfers due to the comparatively large startup time required before any bytes are transferred. This favors a large block size.
  2. Internal fragmentation favors a small block size. This is especially true for small files, which would use only a tiny fraction of a large block and thus waste much more than the 1/2 block average internal fragmentation found for random sizes. 

For some systems, the vast majority of the space used is consumed by the very
largest files. For example, it would be easy to have a few hundred gigabytes
of video. In that case the space efficiency of small files is largely
irrelevant since most of the disk space is used by very large files.

#### Keeping Track of Free Blocks

There are basically two possibilities, a bit map and a linked list.

##### Free Block Bitmap

A region of kernel memory is dedicated to keeping track of the free blocks.
One bit is assigned to each block of the file system. The bit is 1 if the
block is free.

If the block size is 8KB the bitmap uses 1 bit for every 64K bits of disk
space. Thus a 64GB disk would require 1MB of RAM to hold its bitmap.

One can break the bitmap into (fixed size) pieces and apply demand paging.
This saves RAM at the cost of increased I/O.

##### Linked List of Free Blocks

A naive implementation would simply link the free blocks together and just
keep a pointer to the head of the list. Although it wastes no space, this
simple scheme has poor performance since it requires an I/O for every
acquisition or return of a free block.

![free-blocks](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/free-
blocks.png)

In the naive scheme a free disk block contains just one pointer; even though
it could hold a thousand pointers. The improved scheme, shown on the right,
has only a small number of the blocks on the list. Those blocks point not only
to the next block on the list, but also to many other free blocks that are not
directly on the list.

As a result only one in about 1000 requests for a free block requires an I/O,
a great improvement.

Unfortunately, a bad case still remains. Assume the head block on the list is
exhausted, i.e. points only to the next block on the list. A request for a
free block will receive this block, and the next one on the list is brought
it. It is full of pointers to free blocks not on the list (so far so good).

If a free block is now returned we repeat the process and get back to the in-
memory block being exhausted. This can repeat forever, with one extra I/O per
request.

Tanenbaum shows an improvement where you try to keep the one in-memory free
block half full of pointers. Similar considerations apply when splitting and
coalescing nodes in a B-tree.

#### Disk Quotas

Two limits can be placed on disk blocks owned by a given user, the so called
soft and hard limits. A user is never permitted to exceed the hard limit. This
limitation is enforced by having system calls such as write return failure if
the user is already at the hard limit.

A user is permitted to exceed the soft limit during a login session provided
it is corrected prior to logout. This limitation is enforced by forbidding
logins (or issuing a warning) if the user is above the soft limit.

Often files on directories such as /tmp are not counted towards either limit
since the system is permitted to deleted these files when needed.

### 4.4.2 File System Backups (a.k.a. Dumps)

A **physical backup** simply copies every block in order onto a tape or second
disk or the cloud (or other backup media). It is simple and useful for
disaster protection, but not useful for retrieving individual files.

We will study **logical backups**, i.e., dumps that are file and directory
based not simply block based.

Tanenbaum describes the (four phase) unix dump algorithm.

All modern systems support **full** and **incremental** dumps.

  * A level 0 dump is a called a full dump (i.e., dumps everything).
  * A level n dump (n>0) is called an incremental dump and the standard unix utility backs up all files that have changed since the most recent dump of level k<n.
  * Some other dump utilities dump all files that have changed since the most recent dump at level k≤n.
  * Assume you a level 0 dump (i.e. a full dump) is done yearly, a level 4 dump is done every sunday and a level 5 is done every monday-saturday (I personally use this scheme). Thursday's dump will have all files that changed since sunday and thus will be bigger than wednesday's dump. The other style dump will only dump the files that changed since wednesday and hence daily dumps will be about the same size.
  * Restoring a unix dump would require restoring the most recent level-0, level-4, and level-5. The other dump style would require the most recent level-0, **all** level-4s since the last level-0, and **all** level-5s since the last level-4.
  * The system keeps on the disk the dates of the most recent level i dumps for all i so that the dump program can determine which files need to be dumped for a level-k incremental. In Unix these dates are traditionally kept in the file /etc/dumpdates.
  * What about the nodump attribute? 
    * Default policy (for Linux at least) is to dump such files anyway when doing a full dump, but not dump them for incremental dumps.
    * Another way to say this is the nodump attribute is honored for level n dumps if n>0.
    * The dump command has an option to override the default policy (can specify k so that nodump is honored for level n dumps if n>k). 

Traditionally, disks were dumped onto tapes since the latter were cheaper per
byte. Since tape densities are increasing slower than disk densities, an ever
larger number of tapes are needed to dump a disk. This has lead to disk-to-
disk dumps.

Another possibility is to utilize raid, which we study next chapter.

### 4.4.3 File System Consistency

Modern systems have utility programs that check the consistency of a file
system. A different utility is needed for each file system type in the system,
but a wrapper program is often created so that the user is unaware of the
different utilities.

The unix utility is called fsck (file system check) and the windows utility is
called chkdsk (check disk).

  * If the system crashed, it is possible that not all metadata was written to disk. As a result the file system may be inconsistent. These programs check, and often correct, inconsistencies.
  * Scan all i-nodes (or fat) to check that each block is in exactly one file, or on the free list, but **not** both.
  * Also check that the number of links to each file (part of the metadata in the file's i-node) is correct (by looking at all directories).
  * Other checks as well.
  * Offers to fix the errors found (for most errors).

#### Bad blocks on disks

Not so much of a problem now. Disks are more reliable and, more importantly,
disks and disk controllers take care most bad blocks themselves.

### 4.4.4 File System Performance

#### Caching

Demand paging _again_!

Demand paging is a form of caching: Conceptually, the process resides on disk
(the big and slow medium) and only a portion of the process (hopefully a small
portion that is heavily access) resides in memory (the small and fast medium).

The same idea can be applied to files. The file resides on disk but a portion
is kept in memory. The area in memory used to for those file blocks is called
the **buffer cache** or **block cache**.

Some form of LRU replacement is used.

The buffer cache is clearly good and simple for blocks that are only read.

What about writes?

  * The system must update the buffer cache if the file block is present (otherwise subsequent reads will return the old value).
  * If the file block is not present, then a cache block is allocated for it, which likely causes an old file block to be evicted. 

This decision to allocate a cache block for writes that are not present in the
cache is called a write-allocate policy Although no-write-allocate is possible
and sometimes used for memory caches, it performs poorly for disk caching.

  * The major question is whether, on a write to a block that already exists in the cache, the system should write the new value of the block to disk _in addition_ to updating the buffer cache.
  * The simplest alternative is **write through** in which each write is performed at the disk as well. 
    * Since floppy disk drivers adopt a write-through policy, one can remove a floppy as soon as an operation is complete.
    * Write through results in heavy I/O write traffic. 
      * If a block is written many times all the writes are sent the disk. Only the last one was needed.
      * If a temporary file is created, written, read, and deleted, _all_ the disk writes were wasted.
    * No modern system uses write-through for hard drives.
  * The other alternative is **write back**, also known as **copy-back**, in which the disk is **not** updated until the in-memory copy is evicted (i.e., at _replacement_ time). 
    * Write-back generates much less write traffic than write through. Hence all modern systems use write back for hard drives.
    * Trouble if a crash occurs or if the disk is removed before the write back completes (think of a removable flash drive).
    * The system is permitted to write dirty blocks back before they are evicted. It is common for a system to write back all dirty blocks about once a minute. This limits the possible damage, but also the possible gain.
    * Ordered writes. Do not write a block containing pointers until the blocks pointed to have been written. This is especially important if the block pointed to contains pointers since the version of these pointers on disk may be wrong and you are giving a file pointers to some random blocks. 

**Homework:** 32\. The performance of a file system depends upon the cache hit rate (fraction of blocks found in the cache. If it take 1 msec to satisfy a request from the cache, but 40 msec to satisfy a request if a disk read is needed, give a formula for the mean time required to satisfy a request if the hit rate is h. Plot this function for values of h ranging from mo to 1.

#### Block Read Ahead

When the access pattern looks sequential, read ahead is employed. This means
that after completing a read() request for block n of a file, the system
guesses that a read() request for block n+1 will shortly be issued and hence
automatically fetches block n+1.

  * How does the system decide that the access pattern looks sequential? 
    * If a seek system call is issued, the access pattern is not sequential.
    * If a process issues consecutive read() system calls for block n-1 and then n, the access pattern is guessed to be sequential.
  * What if block n+1 is already in the block cache?  
Ans: Don't issue the read ahead.

  * Would it be reasonable to read ahead two or three blocks?  
Ans: Yes.

  * Would it be reasonable to read ahead the entire file?  
Ans: No, it could easily pollute the cache evicting needed blocks, and could
waste considerable disk bandwidth.

#### Reducing Disk Arm Motion

The idea is to try to place near each other blocks that are likely to be used
together.

  1. If the system uses a bitmap for the free list, it can allocate a new block for a file close to the previous block (guessing that the file will be accessed sequentially).
  2. The system can perform allocations in super-blocks, consisting of several contiguous blocks. 
    * The block cache and I/O requests are still in blocks not super-blocks.
    * If the file is accessed sequentially, consecutive blocks of a super-block will be accessed in sequence and these are contiguous on the disk.
  3. For a unix-like file system, the i-nodes can be placed in the middle of the disk, instead of at one end, to reduce the seek time needed to access an i-node followed by a block of the file.
  4. The system can logically divide the disk into **cylinder groups**, each of which is a consecutive group of cylinders. 
    * Each cylinder group has its own free list and, for a unix-like file system, its own space for i-nodes.
    * If possible, the blocks for a file are allocated in the same cylinder group as the i-node.
    * This reduces seek time if consecutive accesses are for the same file. 

### 4.4.5 Defragmenting Disks

If clustering is not done, files can become spread out all over the disk and a
utility (defrag on windows) can be run which makes files contiguous on the
disk.

## 4.5 Example File Systems

### 4.5.A The CP/M File System

CP/M was a very early and simple OS. It ran on primitive hardware with very
little ram and disk space. CP/M had only one directory in the entire system.
The directory entry for a file contained pointers to the disk blocks of the
file. If the file contained more blocks than could fit in a directory entry, a
second entry was used.

### 4.5.1 CD-ROM File Systems

File systems on cdroms do not need to support file addition or deletion and as
a result have no need for free blocks. A CD-R (recordable) does permit files
to be added, but they are always added at the end of the disk. The space
allocated to a file is not recovered even when the file is deleted, so the
(implicit) free list is simply the blocks after the last file recorded.

The result is that the file systems for these devices are quite simple.

#### The ISO9660 File System

This international standard forms the basis for essentially all file systems
on data cdroms (music cdroms are different and are not discussed). Most Unix
systems use iso9660 with the Rock Ridge extensions, and most windows systems
use iso9660 with the Joliet extensions.

The ISO9660 standard permits a single physical CD to be partitioned and
permits a cdrom file system to span many physical CDs. However, these features
are rarely used and we will not discuss them.

Since files do not change, they are stored contiguously and each directory
entry need only give the starting location and file length.

File names are 8+3 characters (directory names just 8) for iso9660-level-1 and
31 characters for -level-2. There is also a -level-3 in which a file is
composed of extents which can be shared among files and even shared within a
single file (i.e. a single physical extent can occur multiple times in a given
file).

Directories can be nested only 8 deep.

#### Rock Ridge Extensions

The Rock Ridge extensions were designed by a committee from the unix community
to permit a unix file system to be copied to a cdrom without information loss.

These extensions included.

  1. The unix rwx bits for permissions.
  2. Major and Minor numbers to support special files, i.e. including devices in the file system name structure.
  3. Symbolic links.
  4. An alternate (long) name for files and directories.
  5. A somewhat kludgy work around for the limited directory nesting levels.
  6. Unix timestamps (creation, last access, last modification).

#### Joliet Extensions

The Joliet extensions were designed by Microsoft to permit a windows file
system to be copied to a cdrom without information loss.

These extensions included.

  1. Long file names.
  2. Unicode.
  3. Arbitrary depth of directory nesting.
  4. Directory names with extensions.

### 4.5.2 The MS-DOS (and Windows) FAT File System

We discussed this linked-list, File-Allocation-Table-based file system
previously. Here we add a little history. More details can be found in [ this
lecture ](http://www.c-jump.com/CIS24/Slides/FAT/lecture.html) from Igor
Kholodov. (A local copy is [here).](kholodov-fat.html)

#### MS-DOS and Early Windows

The FAT file system has been supported since the first IBM PC (1981) and is
still widely used. Indeed, considering the number of cameras, MP3 players, and
smart phones, it is very widely used.

Unlike CP/M, MS-DOS always had support for subdirectories and metadata such as
date and size.

File names were restricted in length to 8+3.

As described previously, the directory entries point to the first block of
each file and the FAT contains pointers to the remaining blocks.

The free list was supported by using a special code in the FAT for free
blocks. You can think of this as a bitmap with a wide bit.

The first version FAT-12 used 12-bit block numbers so a partition could not
exceed 212 blocks. A subsequent release went to FAT-16.

#### The Windows 98 File System

Two changes were made: Long file names were supported and the file allocation
table was switched from FAT-16 to FAT-32. These changes first appeared in the
second release of Windows 95.

##### Long File Names

The hard part of supporting long names was keeping compatibility with the old
8+3 naming rule. That is, new file systems created with windows 98 using long
file names must be accessible if the file system is subsequently used with an
older version of windows that supported only 8+3 file names. The ability for
old systems to read data from new systems was important since users often had
both new and old systems and kept many files on floppy disks that were used on
both systems.

This abiliity to access new objects on old systems is called backwards
compatibility and is not always achieved. For example files produced by new
versions of microsoft word many not be fully comprehended by old versions of
word. The reverse capability, the ability to read old files on new systems, is
much easier to accomplish and is almost always achieved. For example, newer
versions of microsoft word could always read documents produced by older
versions.

Backwards compatibility of Windows file names was achieved by permitting a
file to have two names: a long one and an 8+3 one. The primary directory entry
for a file in windows 98 is the same format as it was in MS-DOS and contains
the 8+3 file name. If the long name fits the 8+3 format, the story ends here.

If the long name does not fit in 8+3, an (often ugly) 8+3 alternate name is
produced and stored in the normal location. The long name is stored in one or
more axillary directory entries adjacent to the main entry. These axillary
entries are set up to appear invalid to the old OS, which (surprisingly)
ignores them.

##### FAT-32

FAT-32 used 32 bit words for the block numbers (actually, it used 28 bits) so
the FAT could be huge (228 entries). Windows 98 kept only a portion of the
FAT-32 table in memory at a time, a form of caching / demand-paging.

### 4.5.3 The Unix V7 File System

I presented the inode system in some detail above. Here we just describe a few
properties of the filesystem beyond the inode structure itself.

  * Each directory entry contains a name and a pointer to the corresponding i-node.
  * The metadata for a file or directory is stored in the corresponding inode.
  * Early unix limited file names to 14 characters, stored in a fixed length field.
  * The name field now is of varying length and file names can be quite long. On my linux system 
    
              touch 255-char-name
        

is OK but

    
              touch 256-char-name
        

is not.

  * To go down a level in the directory hierarchy takes two steps: get the inode, get the file (or subdirectory).
  * This shows how important it is not to parse filenames for each I/O operation, i.e., why the open() system call is important.
  * Do on the blackboard the steps for /a/b/X.

## 4.6 Research on File Systems

## 4.6 Summary

Read

**Remark**: A practice final is on the web site.

# Chapter 5 Input/Output

## 5.1 Principles of I/O Hardware

### 5.1.1 I/O Devices

The most noticeable characteristic of the current ensemble of I/O devices is
their great diversity.

  * Some, e.g. disks, transmit megabytes per second; others, like keyboards, don't transmit a megabyte in their lifetime.
  * Some, like ethernet, are purely electronic; others, like disks are mechanical marvels.
  * A mouse can be put in your pocket; a high-speed printer needs at least two people to move it.
  * Some devices, e.g. a keyboard, are input only. But note that this is in some sense a crazy classification since a keyboard produces output, which is sent to the computer, and receives very little input from the computer (mostly to turn on/off a few lights). Really a keyboard is a transducer, taking mechanical input from a human and producing electronic output for a computer.
  * Similarly, an output only device such as a printer supplies very little output to the computer (perhaps an out&hyphen;of&hyphen;paper indication) but receives voluminous input from the computer. Again it is better thought of as a transducer, converting electronic data from the computer to paper data for humans.
  * Many storage devices are input/output, but again the words can be funny. A disk is viewed as an input device when it is being read, i.e., when it is outputting data; it is viewed as an output device when it is inputting data.
  * Often devices are characterized as **block devices** or as **character devices**. The distinction being that devices like disks are read/written in blocks and individual blocks can be addressed (i.e., not all accesses are sequential). An ethernet interface or a printer has no notion of block or addresses. Instead, it just deals with a stream of characters.
  * However, the block/character device distinction is fuzzy. What about tapes? They read/write blocks and are sort of block addressable (rewind then skip forward). Clocks are weird and hard to classify; they simply generate periodic interrupts. 

### 5.1.2 Device Controllers

To perform I/O typically requires both mechanical and electronic activity. The
mechanical component is called the device itself. The electronic component is
called a _controller_ or an _adapter_.

The controllers _are_ the devices as far as the OS is concerned. That is, the
OS code is written with the controller specification in hand not with the
device specification.

  * A controller abstracts away some of the low level features of the devices it controls. For example, a disk controller performs error checking and assembles the bit stream coming off the disk into blocks of bytes.
  * Graphics controllers do a great deal. They often contain processors at least as powerful as the CPU on which the OS and applications run.
  * In the old days controllers handled interleaving of sectors. Sectors are interleaved if the controller or CPU cannot handle the data rate and would otherwise have to wait a full revolution between sectors. This is not a concern with modern systems since the electronics have increased in speed faster than the devices and now all disk controllers can handle the full data rate of the disks they support.

###  5.1.3 Memory-Mapped I/O (vs I/O Space Instructions)

Consider a disk controller processing a read request. The goal is to copy data
from the disk to some portion of the central memory. How is this to be
accomplished?

The controller contains a microprocessor and memory, and is connected to the
disk (by wires). When the controller requests a sector from the disk, the
sector is transmitted to the control via the wires and is stored by the
controller in **its** memory.

The separate processor and memory on the controller gives rise to two
questions.

  1. How does the OS request that the controller, which is running on another processor, perform an I/O and how are the parameters of the request transmitted to the controller?
  2. How is the data that has been read from the disk moved from the controller's memory to the general system memory? Similarly, how is data that is to be written to the disk moved from the system memory to the controller's memory?

Typically the interface the controller presents to the OS consists of a few
registers located on the controller board.

  * These are memory locations into which the OS writes information such as the sector to access, read vs. write, length, where in system memory to put the data (for a read) or from where to take the data (for a write). The controller reads these registers.
  * There are also devices registers that the OS reads and the controller writes, such as the status of the controller, any errors that were detected, etc.
  * There is also typically a device register that acts as a go button.

So the first question above becomes, how does the OS read and write the device
register?

  * With **memory-mapped I/O** the device registers appear as normal memory. All that is needed is to know at which address each device register appears. Then the OS uses normal load and store instructions to read and write the registers.
  * Some systems instead have a special I/O space into which the registers are mapped. In this case special I/O space instructions are used to accomplish the loads and stores.
  * From a conceptual point of view there is no difference between the two models, but the implementations differ 
    1. Memory-mapped I/O is a more elegant solution in that it uses an existing mechanism to accomplish a second objective.
    2. Since normal loads and stores are used for memory-mapped I/O, the algorithm can be written in a high-level language. Assembly language is needed for I/O space instructions since such instructions cannot be expressed in (normal) high-level languages.
    3. A memory-mapped implementation must arrange that these addresses are sent to the appropriate bus and must insure that they are not cached.
  * The remainder of these notes are written assuming a memory mapped implementation.
![dma](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/dma.png)

### 5.1.4 Direct Memory Access (DMA)

We now address the second question, moving data between the controller and the
main memory. Recall that the disk controller, when processing a read request,
pulls the desired data from the disk to its own buffer. Similarly, it pushes
data from the buffer to the disk when processing a write).

Without DMA, i.e., with **programmed I/O** (PIO), the read is completed by
having the cpu issue loads and stores (assuming the controller buffer is
memory mapped, or uses I/O instructions if it is not) to copy the data from
the buffer to the desired memory locations.

With DMA the controller writes the main memory itself, without intervention of
the CPU.

Clearly DMA saves CPU work. However, the number of memory references does not
decrease so the CPU may be delayed due to busy memory.

An important point is that there is less data movement with DMA so the buses
are used less and the entire operation takes less time. Compare the two blue
arrows vs. the single red arrow.

Since PIO is pure software it is easier to change, which is an advantage.

Initiating DMA requires a number of bus transfers from the CPU to the
controller to write the device registers. So DMA is most effective for large
transfers where the setup is amortized.

A serious complexity of DMA is that the bus must support multiple masters and
hence requires _arbitration_, which leads to issues similar to those we faced
with critical sections.

Why have the buffer? Why not just go from the disk straight to the memory?

  1. Speed matching.  
The disk supplies data at a fixed rate, which might exceed the rate the memory
can accept it. In particular the memory might be busy servicing a request from
the processor or from another DMA controller.  
Alternatively, the disk might supply data at a slower rate than the memory
(and memory bus) can handle thus under-utilizing an important system resource.

  2. Error detection and correction.  
The disk controller verifies the checksum written on the disk.

**Homework:** 15\. A local area network is used as follows. The user issues a system call to write data packets to the network. The operating system then copies the data to a kernel buffer. Then it copies the data to the network controller board. When all the bytes are safely inside the controller, they are sent over the network at a rate of 10 megabits/sec. The receiving network controller stores each bin a microsecond after it is sent. When the last bit arrives, the destination CPU is interrupted, and the kernel copies the newly arrived packet to a kernel buffer to inspect it. Once it has figured out which user the packet is for, the kernel copies the data to the user space. If we assume that each interrupt and its associated processing takes 1 msec, that packets are 1024 bytes (ignore the headers), and that copying a byte takes 1 microsecond, what is the maximum rate at which one process can pump data to another? Assume that the sender is blocked until the work is finished at the receiving side and acknowledegment comes back. For simplicity, assume that the time to get the acknowledgement back is so small it can be ignored.

### 5.1.5 Interrupts Revisited

#### Precise and Imprecise Interrupts

## 5.2 Principles of I/O Software

As with any large software system, good design and layering is important.

### 5.2.1 Goals of the I/O Software

#### Device Independence

We want to have most of the OS to be unaware of the characteristics of the
specific devices attached to the system. (This principle of device
independence is not limited to I/O; we also want the OS to be largely unaware
of the specific CPU employed.)

This objective has been accomplished quite well for files stored on various
devices. Most of the OS, including the file system code, and most applications
can read or write a file without knowing if the file is stored on an internal
SATA hard disk, an external USB SCSI disk, an external USB Flash Ram, a tape,
or (for read-only applications) a CD-ROM.

This principle also applies for user programs reading or writing streams. A
program reading from standard input, which is normally the user's keyboard can
be told to instead read from a disk file with no change to the application
program. Similarly, standard output can be redirected to a disk file. However,
the low-level OS code dealing with disks is rather different from that dealing
keyboards and (character-oriented) terminals.

One can say that device independence permits programs to be implemented as if
they will read and write generic or abstract devices, with the actual devices
specified at run time. Although writing to a disk has differences from writing
to a terminal, Unix **cp**, DOS **copy**, and many programs we compose need
not be aware of these differences.

However, there are devices that really are special. The graphics interface to
a monitor (that is, the graphics interface presented by the video controller--
often called a ``video card'') does not resemble the ``stream of bytes'' we
see for disk files.

**Homework:** What is device independence?

#### Uniform naming

We have already discussed the value of the name space implemented by file
systems. There is no dependence between the name of the file and the device on
which it is stored. So a file called IAmStoredOnAHardDisk might well be stored
on a floppy disk.

More interesting once a device is mounted on (Unix) directory, the device is
named exactly the same as the directory was. So if a CD-ROM was mounted on
(existing) directory /x/y, a file named joe on the CD-ROM would now be
accessible as /x/y/joe.

#### Error handling

There are several aspects to error handling including: detection, correction
(if possible) and reporting.

  1. Detection should be done as close to where the error occurred as possible before more damage is done (fault containment). Moreover, the error may be obvious at the low level, but harder to discover and classify if the erroneous data is passed to higher level software.
  2. Correction is sometimes easy, for example ECC memory does this automatically (but the OS wants to know about the error so that it can request replacement of the faulty chips before unrecoverable double errors occur). Other easy cases include successful retries for failed ethernet transmissions. In this example, while logging is appropriate, it is quite reasonable for no action to be taken.
  3. Error reporting tends to be awful. The trouble is that the error occurs at a low level but by the time it is reported the context is lost.

#### Creating the illusion of synchronous I/O

I/O _must_ be asynchronous for good performance. That is the OS _cannot_
simply wait for an I/O to complete. Instead, it proceeds with other activities
and responds to the interrupt that is generated when the I/O has finished.

    
    
      Read X
      Y = X+1
      Print Y
    

Users (mostly) want no part of this. The code sequence on the right should
print a value one greater than that read. But if the assignment is performed
before the read completes, the wrong value can easily be printed.

Performance junkies sometimes _do_ want the asynchrony so that they can have
another portion of their program executed while the I/O is underway. That is,
they implement a mini-scheduler in their application code.

See [this message](asyncIO-ingo) from linux kernel developer Ingo Molnar for
his take on asynchronous IO and kernel/user threads/processes. You can find
the entire discussion [ here.
](http://www.ussg.iu.edu/hypermail/linux/kernel/0701.3/2371.html)

#### Buffering

Buffering is often needed to hold data for examination prior to sending it to
its desired destination.

When two buffers are used the producer can deposit more data while the old
data is being consumed. (Recall the bounded buffer a.k.a. producer-consumer
problem).

Since this involves copying the data, which can be expensive, modern systems
try to avoid as much buffering as possible. This is especially noticeable in
network transmissions, where the data could conceivably be copied _many_
times.

  1. From user space to kernel space as part of the write system call.
  2. From kernel space to a kernel I/O buffer.
  3. From the I/O buffer to a buffer on the network adaptor.
  4. From the adapter on the source to the adapter on the destination.
  5. From the destination adapter to an I/O buffer.
  6. From the I/O buffer to kernel space.
  7. From kernel space to user space as part of the read system call.

I am not sure if any systems actually do all seven.

#### Sharable vs. Dedicated Devices

For devices like printers and CD-ROM drives, only one user at a time is
permitted. These are called **serially reusable** devices, which we studied in
the deadlocks chapter. Devices such as disks and ethernet ports can, on the
contrary, be shared by concurrent processes without any deadlock risk.

### 5.2.2 Programmed I/O

As mentioned just above, with programmed I/O the main processor (i.e., the one
on which the OS runs) moves the data between memory and the device. This is
the most straightforward method for performing I/O.

One question that arises is, How does the processor know when the device is
ready to accept or supply new data?.

    
    
      while (device-not-available)
        do-useful-work
    

The simplest implementation is shown on the right. The processor, when it
seeks to use a device, loops continually querying the device status, until the
device reports that it is free. This is called **polling** or **busy
waiting**.

If we poll infrequently (and do useful work in between), there can be a
significant delay from when the previous I/O is complete to when the OS
detects the device availability.

If we poll frequently (and thus are able to do little useful work in between)
and the device is (sometimes) slow, polling is clearly wasteful.

The extreme case is where the process does nothing between polls. For a slow
device this can take the CPU out of service for a significant period. This bad
situation leads us to ... .

### 5.2.3 Interrupt-Driven (Programmed) I/O

As we have just seen, a difficulty with polling is determining the frequency
with which to poll. Another problem is that the OS must continually return to
the polling loop, i.e., we must arrange that do-useful-work takes the desired
amount of time. Really we want the device to tell the CPU when it is
available, which is exactly what an interrupt does.

The device interrupts the processor when it is ready and an interrupt handler
(a.k.a. an interrupt service routine) then initiates transfer of the next
datum.

Normally interrupt schemes perform better than polling, but not always since
interrupts are expensive on modern machines. To minimize interrupts, better
controllers often employ ...

### 5.2.4 I/O Using DMA

We discussed DMA above.

An additional advantage of dma, not mentioned above, is that the processor is
interrupted only at the end of a command not after each datum is transferred.
Many devices receive a character at a time, but with a dma controller, an
interrupt occurs only after a buffer has been transferred.

## 5.3 I/O Software Layers

Layers of abstraction as usual prove to be effective. Most systems are
believed to use the following layers (but for many systems, the OS code is not
available for inspection).

  1. User-level I/O routines.
  2. Device-independent (kernel-level) I/O software.
  3. Device drivers.
  4. Interrupt handlers.

We will give a bottom up explanation.

### 5.3.1 Interrupt Handlers

We discussed behavior similar to an interrupt handler before when studying
page faults. Then it was called assembly-language code. A difference is that
page faults are caused by specific user instructions, whereas interrupts just
happen. However, the assembly-language code for a page fault accomplishes
essentially the same task as the interrupt handler does for I/O.

In the present case, we have a process blocked on I/O and the I/O event has
just completed. So the goal is to make the process ready and then call the
scheduler. Possible methods are.

  * Releasing a semaphore on which the process is waiting.
  * Sending a message to the process.
  * Inserting the process table entry onto the ready list.

Once the process is ready, it is up to the scheduler to decide when it should
run.

### 5.3.2 Device Drivers

We gave an overview before.

Device drivers form the portion of the OS that is tailored to the
characteristics of individual controllers. They form the dominant portion of
the source code of the OS since there are hundreds of drivers. Normally some
mechanism is used so that the only drivers loaded on a given system are those
corresponding to hardware actually present.

Indeed, modern systems often have loadable device drivers, which are loaded
dynamically when needed. This way if a user buys a new device, no changes to
the operating system are needed. When the device is installed it will be
detected during the boot process and the corresponding driver is loaded.

![components](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/components.pn
g)

Sometimes an even fancier method is used and the device can be plugged in
while the system is running (USB devices are like this). In this case it is
the device insertion that is detected by the OS and that causes the driver to
be loaded.

Some systems can dynamically **un**load a driver, when the corresponding
device is unplugged.

The driver has two parts corresponding to its two access points. The figure on
the right, which we first encountered at the beginning of the course, helps
explain the two parts and their names.

The driver is accessed by the main line OS via the envelope in response to an
I/O system call. The portion of the driver accessed in this way is sometimes
called the top part.

The driver is also accessed by the interrupt handler when the I/O completes
(this completion is signaled by an interrupt). The portion of the driver
accessed in this way is sometimes called the bottom part.

In some system the drivers are implemented as user-mode processes. Indeed,
Tannenbaum's MINIX system works that way, and in previous editions of the
text, he describes such a scheme. However, most systems have the drivers in
the kernel itself and the 3e describes this scheme. I previously included both
descriptions, but have eliminated the user-mode process description (actually
I greyed it out).

![unblocking-1](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/unblocking-
1.png)

#### Driver in the Kernel

The three-part diagram to the right and below shows the high-level actions
that occur. On the right we see the initial state, process A is running and is
about it issue a read system call. Process B is ready to run; it is waiting to
be scheduled. (Although only A and B are shown, there may be many other
processes ready and running as well.)

Below we see later states. The second diagram shows the situation after
process A has issued its read system call. The process is now blocked waiting
for the read to complete. The scheduler has chosen to run process B. In the
third diagram, the read is complete and process A is now ready. Perhaps the
scheduler will run it soon.

![unblocking-2-3](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/unblockin
g-2-3.png)  
  

##### A Detailed view

What follows is the Unix-like view in which the driver is invoked by the OS
acting in behalf of a user process (alternatively stated, the process shifts
into kernel mode). Thus one says that the scheme follows a self-service
paradigm in that the process itself (now in kernel mode) executes the driver.

The numbers in the diagram to the right correspond to the numbered steps in
the description that follows. The previous diagram showed the state of
processes A and B at steps 1, 6, and 9 in the execution sequence.

![driver](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/driver.png)

  1. The currently running process (say A) issues an I/O system call.
  2. The main line, machine independent, OS prepares a generic request and calls (the top part of) the driver. 
    1. If the driver was idle (i.e., the controller was idle), the driver writes device registers on the controller ending with a command for the controller to begin the actual I/O (the go button mentioned previously).
    2. If the controller was busy (doing work the driver gave it previously), the driver simply queues the current request (the driver dequeues this request below).
  3. The driver jumps to the scheduler indicating that the current process should be blocked.
  4. The scheduler blocks A and runs (say) B.
  5. B starts running; eventually an interrupt occurs (the I/O for A has completed).
  6. The interrupt handler is invoked.
  7. The interrupt handler invokes (the bottom part of) the driver. 
    1. The driver stores information concerning the I/O just performed for process A. The information might include data read and surely includes status (error, OK).
    2. The top part is called to start another I/O if the queue is nonempty. We know the controller is free. Why?  
Answer: We just received an interrupt saying so.

  8. The driver jumps to the scheduler indicating that process A should be made ready.
  9. The scheduler picks a ready process to run. Assume it picks A.
  10. A resumes in the driver, which returns to the main line, which returns to the user code.

#### Driver as a Process (Less Detailed Than Above)

Actions that occur when the user issues an I/O request.

  1. The main line OS prepares a generic request (e.g. read, not read using Buslogic BT-958 SCSI controller) for the driver and the driver is awakened. Perhaps a message is sent to the driver to do both jobs.
  2. The driver wakes up. 
    1. If the driver was idle (i.e., the controller is idle), the driver writes device registers on the controller ending with a command for the controller to begin the actual I/O.
    2. If the controller is busy (doing work the driver gave it), the driver simply queues the current request (the driver dequeues this below). 
  3. The driver blocks waiting for an interrupt or for more requests. 

Actions that occur when an interrupt arrives (i.e., when an I/O has been
completed).

  1. The driver wakes up.
  2. The driver informs the main line perhaps passing data and surely passing status (error, OK).
  3. The driver finds the next work item or blocks. 
    1. If the queue of requests is non-empty, dequeue one and proceed as if just received a request from the main line.
    2. If queue is empty, the driver blocks waiting for an interrupt or a request from the main line. 

### 5.3.3 Device-Independent I/O Software

The device-independent code cantains most of the I/O functionality, but not
most of the code since there are _very many_ drivers. All drivers of the same
class (say all hard disk drivers) do essentially the same thing in slightly
different ways due to slightly different controllers.

#### Uniform Interfacing for Device Drivers

As stated above the bulk of the OS code is made of device drivers and thus it
is important that the task of driver writing not be made more difficult than
needed. As a result each class of devices (e.g. the class of all disks) has a
defined driver interface to which all drivers for that class of device
conform. The device independent I/O portion processes user requests and calls
the drivers.

#### Naming

Naming is again an important O/S functionality. In addition it offers a
consistent interface to the drivers. The Unix method works as follows

  * Each device is associated with a special file in the /dev directory.
  * The i-nodes for these files contain an indication that these are special files and also contain so called major and minor device numbers.
  * The major device number gives the number of the driver. (These numbers are rather ad hoc, they correspond to the position of the function pointer to the driver in a table of function pointers.)
  * The minor number indicates for which device (e.g., which scsi cdrom drive) the request is intended.
  * For example my office workstation has two scsi disks (one is external via USB, but that is not relevant). The two disks are named by linux sda and sdb. The partitions of sda are named sda1, sda2, etc. From the following listing we can see that the scsi driver is number 8 and that numbers are reserved for 15 partitions for each scsi drive, which is the limit scsi supports. The result is as follows. 
    
              allan dev # ls -l /dev/sd*
          brw-r----- 1 root disk 8,  0 Apr 25 09:55 /dev/sda
          brw-r----- 1 root disk 8,  1 Apr 25 09:55 /dev/sda1
          brw-r----- 1 root disk 8,  2 Apr 25 09:55 /dev/sda2
          brw-r----- 1 root disk 8,  3 Apr 25 09:55 /dev/sda3
          brw-r----- 1 root disk 8,  4 Apr 25 09:55 /dev/sda4
          brw-r----- 1 root disk 8,  5 Apr 25 09:55 /dev/sda5
          brw-r----- 1 root disk 8,  6 Apr 25 09:55 /dev/sda6
          brw-r----- 1 root disk 8, 16 Apr 25 09:55 /dev/sdb
          brw-r----- 1 root disk 8, 17 Apr 25 09:55 /dev/sdb1
          brw-r----- 1 root disk 8, 18 Apr 25 09:55 /dev/sdb2
          brw-r----- 1 root disk 8, 19 Apr 25 09:55 /dev/sdb3
          brw-r----- 1 root disk 8, 20 Apr 25 09:55 /dev/sdb4
          allan dev #
        

#### Protection

A wide range of possibilities are actually done in real systems. Including
both extreme examples of everything is permitted and nothing is (directly)
permitted.

  * In ms-dos any process can write to any file. Presumably, our offensive nuclear missile launchers never ran dos.
  * In IBM 360/370/390 mainframe OS's, normal processors do not access devices. Indeed the main CPU doesn't issue the I/O requests. Instead an I/O channel is used and the mainline constructs a channel program and tells the channel to invoke it.
  * Unix uses normal rwx bits on files in /dev (I don't believe x is used). 

#### Buffering

Buffering is necessary since requests come in a sizes specified by the user
and data is delivered by reads and accepted by writes in sizes specified by
the device. Buffering is also important so that a user process using getchar()
in C or the Scanner in java is not blocked and unblocked for each character
read.

The text describes double buffering and circular buffers, which are important
programming techniques, but are not specific to operating systems.

#### Error Reporting

#### Allocating and Releasing Dedicated Devices

The system must enforce **exclusive access** for non-shared devices like CD-
ROMs. We discussed the issues involved when studying deadlocks.

### 5.3.4 User-Space Software

A good deal of I/O software is actually executed by unprivileged code running
in user space. This code includes library routines linked into user programs,
standard utilities, and daemon processes.

If one uses the strict definition that the operating system consists of the
(supervisor-mode) kernel, then this I/O code is not part of the OS. However,
very few use this strict definition.

#### Library Routines

Some library routines are very simple and just move their arguments into the
correct place (e.g., a specific register) and then issue a trap to the kernel
to do the real work.

I think everyone considers these routines to be part of the operating system.
Indeed, they implement the published user interface to the OS. For example,
when we specify the (Unix) read system call by  
`   count = read (fd, buffer, nbytes)  
` as we did in chapter 1, we are really giving the parameters and return value
of such a library routine.

Although users could write these routines, it would make their programs non-
portable and would require them to write in assembly language since neither
trap nor specifying individual registers is available in high-level languages.

Other library routines, notably standard I/O (stdio) in Unix, are definitely
not trivial. For example consider the formatting of floating point numbers
done in System.out.printf() and the reverse operation done by the Scanner in
nextInt().

In unix-like systems the graphics libraries and the gui itself are outside the
kernel. Graphics libraries are quite large and complex. In windows, the gui is
inside the kernel.

#### Utilities and Daemons

Printing to a local printer is often performed in part by a regular program
(lpr in Unix) that copies (or links) the file to a standard place, and in part
by a daemon (lpd in Unix) that reads the copied files and sends them to the
printer. The daemon might be started when the system boots.

Note that this implementation of printing uses **spooling**, i.e., the file to
be printed is copied somewhere by lpr and then the daemon works with this
copy. Mail uses a similar technique (but generally it is called queuing, not
spooling).

### 5.3.A Summary

![IO layers](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/IO-layers.png)

The diagram on the right shows the various layers and some of the actions that
are performed by each layer.

The arrows show the flow of control. The blue downward arrows show the
execution path made by a request from user space eventually reaching the
device itself. The red upward arrows show the response, beginning with the
device supplying the result for an input request (or a completion
acknowledgement for an output request) and ending with the initiating user
process receiving its response.

**Homework:** 14\. In which of the four I/O software layers is each of the following done.

  1. Computing the track, sector ahd head for a disk read.
  2. Writing commands to the device registers.
  3. Checking to see if the user is permitted to use the device.
  4. Converting binary integers to ASCII for printing.

**Homework:** 16\. Why are output files for the printer normally spooled on disk before being printed?

## 5.4 Disks

The ideal storage device is

  1. Fast
  2. Big (in capacity)
  3. Cheap
  4. Impossible

When compared to central memory, disks are big and cheap, but slow.

### 5.4.1 Disk Hardware

#### Magnetic Disks (Hard Drives)

Show a real disk opened up and illustrate the components.

  * Platter
  * Surface
  * Head
  * Track
  * Sector
  * Cylinder
  * Seek time
  * Rotational latency
  * Transfer rate

Consider the following characteristics of a disk.

  * RPM (revolutions per minute).
  * Seek time. This is actually quite complicated to calculate since you have to worry about, acceleration, travel time, deceleration, and "settling time".
  * Rotational latency. The average value is the time for (approximately) one half a revolution.
  * Transfer rate. This is determined by the RPM and bit density.
  * Sectors per track. This is determined by the bit density.
  * Tracks per surface (i.e., the number of cylinders). This is determined by the bit density.
  * Tracks per cylinder (i.e, the number of surfaces).

Overlapping I/O operations is important when the system has more than one
disk. Many disk controllers can do overlapped seeks, i.e. issue a seek to one
disk while another disk is already seeking.

As technology improves the space taken to store a bit decreases, i.e., the bit
density increases. This changes the number of cylinders per inch of radius
(the cylinders are closer together) and the number of bits per inch along a
given track.

Despite what Tanenbaum says later, it is not true that when one head is
reading from cylinder C, all the heads can read from cylinder C with no
penalty. It is, however, true that the penalty is very small.

#### Choice of Block Size

Current commodity disks for commodity computers require a little less than
10ms. before transferring the first byte and then transfer roughly 100K bytes
per ms. (if contiguous). Specifically

  * The rotation rate is normally 7200 RPM with 10k, 15k and 20k available.
  * Recall that 6000 RPM is 100 rev/sec or one rev per 10ms. So half a revolution (the average rotation needed to reach a given point) is less than 5ms.
  * Transfer rates are around 100MB/sec = 100KB/ms.
  * Seek time is around 5ms.

This is quite extraordinary. For a large **sequential** transfer, in the first
10ms, no bytes are transmitted; in the next 10ms, 1,000,000 bytes are
transmitted. The analysis suggests using large disk blocks, 100KB or more.

But the internal fragmentation would be severe since many files are small.
Moreover, transferring small files would take longer with a 100KB block size.

In practice typical block sizes are 4KB-8KB.

Multiple block sizes have been tried (e.g., blocks are 8KB but a file can also
have fragments that are a fraction of a block, say 1KB).

Some systems employ techniques to encourage consecutive blocks of a given file
to be stored near each other. In the best case, logically sequential blocks
are also physically sequential and then the performance advantage of large
block sizes is obtained without the disadvantages mentioned.

In a similar vein, some systems try to cluster related files (e.g., files in
the same directory).

**Homework:** Consider a disk with an average seek time of 5ms, an average rotational latency of 5ms, and a transfer rate of 40MB/sec.

  1. If the block size is 1KB, how long would it take to read a block?
  2. If the block size is 100KB, how long would it take to read a block?
  3. If the goal is to read 1K, a 1KB block size is better as the remaining 99KB are wasted. If the goal is to read 100KB, the 100KB block size is better since the 1KB block size needs 100 seeks and 100 rotational latencies. What is the minimum size request for which a disk with a 100KB block size would complete faster than one with a 1KB block size? 

#### Virtual Geometry and LBA (Logical Block Addressing)

Originally, a disk was implemented as a three dimensional array  
      Cylinder#, Head#, Sector#  
The cylinder number determined the cylinder, the head number specified the
surface (recall that there is one head per surface), i.e., the head number
determined the track within the cylinder, and the sector number determined the
sector within the track.

But there is something wrong here. An outer track is longer (in centimeters)
than an inner track, but each stores the same number of sectors. Essentially
some space on the outer tracks was wasted.

Later disks lied. They said they had a virtual geometry as above, but really
had more sectors on outer tracks (like a ragged array). The electronics on the
disk converted between the published virtual geometry and the real geometry.

Modern disk continue to lie for backwards compatibility, but also support
Logical Block Addressing in which the sectors are treated as a simple one
dimensional array with no notion of cylinders and heads.

#### RAID (Redundant Array of Inexpensive Disks)

The name and its acronym RAID came from Dave Patterson's group at Berkeley.
IBM changed the name to Redundant Array of _Independent_ Disks. I wonder why?

The basic idea is to utilize multiple drives to simulate a single larger
drive, but with redundancy and increased performance.

The different RAID configurations are often called different levels, but this
is not a good name since there is no hierarchy and it is not clear that higher
levels are better than low ones. However, the terminology is commonly used so
I will follow the trend and describe them level by level, but having very
little to say about some levels.

  0. Striping.  
Consecutive blocks are interleaved across the multiple drives. The is no
redundancy so it is strange to have it called RAID, but it is. Recall that a
block may consist of multiple sectors.

  1. Mirroring.  
The next level simply replicates the previous one. That is, the number of
drives is doubled and two copies of each block are written, one in each of the
two replicas. A read may access either replica. One might think that both
replicas are read and compared, but this is not done, the drives themselves
have check bits. The reason for having two replicas is to survive a single
disk failure. In addition, read time is improved since the heads on one set of
drives may be closer to the desired block.

  2. Synchronized disks, bit interleaved, multiple Hamming checksum disks.  
I don't believe this scheme is currently used.

  3. Synchronized disks, bit interleaved, single parity disk.  
I don't believe this scheme is currently used.

  4. Striping plus a parity disk.  
Use N (say 4) data disks and one parity disk. Data is striped across the data
disks and the bitwise parity of these blocks is written in the corresponding
block of the parity disk.

    * On a read, if the block is bad (e.g., if the entire disk is bad or even missing), the system automatically reads the other blocks in the stripe and the parity block in the stripe. Then the missing block is just the bitwise exclusive or (aka XOR) of all these blocks.
    * For reads this is very good. The failure free case has no penalty (beyond the space overhead of the parity disk). The error case requires (N-1)+1=N (say 4) reads.
    * A serious concern is the small write problem. Writing a sector requires 4 I/Os: Read the old data sector, compute the change, read the parity, compute the new parity, write the new parity and the new data sector. Hence one sector I/O became 4, which is a 300% penalty. Writing a full stripe is not bad. Compute the parity of the N (say 4) data sectors to be written and then write the data sectors and the parity sector. Thus 4 sector I/Os become 5, which is only a 25% penalty and is smaller for larger N, i.e., larger stripes.
  5. Rotated parity.  
That is, for some stripes, disk 1 has the parity block; for others stripes,
disk 2 has the parity; etc. The purpose is to avoid having a single parity
disk since that disk is needed for all small writes and could easily become a
point of contention.

  6. Additional parity blocks.  
Able to survive multiple faults. In particular, can survive a fault while
rebuilding from a fault.

### 5.4.2 Disk Formatting

### 5.4.3 Disk Arm Scheduling Algorithms

There are three components to disk response time: seek, rotational latency,
and transfer time. Disk arm scheduling is concerned with minimizing seek time
by reordering the requests.

These algorithms are relevant only if there are several I/O requests pending.
For many PCs, the system is so underutilized that there are rarely multiple
outstanding I/O requests and hence no scheduling is possible. At the other
extreme, many large servers, are I/O bound with significant queues of pending
I/O requests. For these systems, effective disk arm scheduling is crucial.

Although disk scheduling algorithms are performed by the OS, they are also
sometimes implemented in the electronics on the disk itself. The disks I
brought to class were somewhat old so I suspect those didn't implement
scheduling, but the then-current operating systems definitely did.

We study the following algorithms all of which are quite simple.

  1. FCFS (First Come First Served).  
The most primitive. Some would called this no scheduling, but I wouldn't.

  2. Pick.  
Same as FCFS but pick up requests for cylinders that are passed on the way to
the next FCFS request.

  3. SSTF or SSF (Shortest Seek (Time) First).  
Use the greedy algorithm and go to the closest requested cylinder. This
algorithm can starve requests. To prevent starvation, one can periodically
enter a FCFS mode, but SSTF would still be unfair. Typically, cylinders in the
middle receive better service than do cylinders on both extremes.

  4. Scan (Look, Elevator).  
This is the method used by an old fashioned jukebox (remember Happy Days) and
by elevators.

Those jukeboxes stole coins since requesting an already requested song was a
nop.

The disk arm proceeds in one direction picking up all requests until there are
no more requests in this direction at which point it goes back the other
direction. This favors requests in the middle, but can't starve any requests.

  5. N-step Scan.  
This is what the natural implementation of Scan actually does. The idea is
that requests are serviced in batches. Specifically, it works as follows.

    * While the disk is servicing a Scan direction, the controller gathers up new requests and sorts them.
    * At the end of the current sweep, the new list becomes the next sweep.
    * Compare this to selfish round robin (SRR) with a≥b=0. 
  6. C-Scan (C-look, Circular Scan/Look).  
Similar to Scan but only service requests when moving in one direction. Let's
assume it services requests when the head is moving from low-numbered
cylinders to high-numbered one. When there are no pending requests for a
cylinder with number higher than the present head location, the head is sent
to the lowest-numbered, requested cylinder. C-Scan doesn't favor any spot on
the disk. Indeed, it treats the cylinders as though they were a clock, i.e.,
after the highest numbered cylinder comes cylinder 0.

#### Minimizing Rotational Latency

Once the heads are on the correct cylinder, there may be several requests to
service. All the systems I know, use Scan based on sector numbers to retrieve
these requests.  
**Question**: Why in this case is Scan same as C-Scan?  
**Answer**: Because the disk rotates in only one direction.

The above is certainly correct for requests to the same track. If requests are
for different tracks on the same cylinder, a question arises of how fast the
disk can switch from reading one track to another on the same cylinder. There
are two components to consider.

  1. How fast can it switch the electronics so that the signal from a different head is the one outputted by the disk?
  2. If the disk are is positioned so that one head is over cylinder k, are all the heads _exactly_ over cylinder k. 

The electronic switching is very fast. I doubt that would be an issue. The
second point is more problematic. I know it was not true in the 1980s: I
proposed a disk in which all tracks in a cylinder were read simultaneously and
coupled this parallel readout disk with with some network we had devised.
Alas, a disk designer explained to me that the heads are _not_ perfectly
aligned with the tracks.

**Homework:** 31\. Disk requests come into to the disk driver for sylinders 10, 22, 20, 2, 40, 6, and 38, in that order. A seek takes 6 ms per cylinder. How much seek time is needed for

  1. First come, first served.
  2. Closest cylinder next.
  3. Elevator algorithm (initially moving upward).

**Homework:** 33\. A salesman claimed that their version of Unix was very fast. For example, their disk driver used the elevator algorithm to reorder requests for different cylinders. In addition, the driver queued multiple requests for the same cylinder in sector order. Some hacker bought a version of the OS and tested it with a program that read 10,000 blocks randomly chosen across the disk. The new Unix was not faster than an old one that did FCFS for all requests. What happened?

#### Track Caching

Often the disk/controller caches (a significant portion of) the entire track
whenever it access a block, since the seek and rotational latency penalties
have already been paid. In fact modern disks have multi-megabyte caches that
hold many recently read blocks. Since modern disks cheat and don't have the
same number of blocks on each track, it is better for the disk electronics
(and not the OS or controller) to do the caching since the disk is the only
part of the system to know the true geometry.

### 5.4.4 Error Handling

Most disk errors are handled by the device/controller and not the OS itself.
That is, disks are manufactured with more sectors than are advertised and
spares are used when a bad sector is referenced. Older disks did not do this
and the operating system would form a secret file of bad blocks that were
never to be used.

### 5.4.A Ram Disks

  * Fairly clear. Organize a region of memory as a set of blocks and pretend it is a disk.
  * A problem is that memory is volatile.
  * Often used during OS installation, before disk drivers are available (there are many types of disk but all memory looks the same so only one ram disk driver is needed). 

### 5.4.5 Stable Storage

Skipped.

![clock](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams/clock.png)

## 5.5 Clocks (Timers)

### 5.5.1 Clock Hardware

The hardware is simple. It consists of

  * An oscillator that generates a pulse at a known fixed frequency.
  * A counter that is decremented at each pulse.
  * A register that can be used to reload the counter.
  * Electronics that generate an interrupt whenever the counter reaches zero. 

The counter reload can be automatic or under OS control. If it is done
automatically, the interrupt occurs periodically (the frequency is the
oscillator frequency divided by the value in the register).

The value in the register can be set by the operating system and thus this
**programmable clock** can be configured to generate periodic interrupts and
any desired frequency (providing that frequency divides the oscillator
frequency).

### 5.5.2 Clock Software

As we have just seen, the clock hardware simply generates a periodic
interrupt, called the **clock interrupt**, at a set frequency. Using this
interrupt, the OS software can accomplish a number of important tasks.

#### Time of Day (TOD)

The basic idea is to increment a counter each clock tick (i.e., each
interrupt). The simplest solution is to initialize this counter at boot time
to the number of ticks since a fixed date (Unix traditionally uses midnight, 1
January 1970). Thus the counter always contains the number of ticks since that
date and hence the current date and time is easily calculated. Two questions
arise.

  1. From what value is the counter initialized?
  2. What about overflow?

Three methods are used for initialization. The system can contact one or more
know time sources (see the Wikipedia entry for NTP), the human operator can
type in the date and time, or the system can have a battery-powered, backup
clock. The last two methods only give an approximate time.

Overflow is a real problem if a 32-bit counter is used. In this case two
counters are kept, the low-order and the high-order. Only the low order is
incremented each tick; the high order is incremented whenever the low order
overflows. That is, a counter with twice as many bits is simulated.

#### Time Quantum for Round Robin Scheduling

The system decrements a counter at each tick. The quantum expires when the
counter reaches zero. The counter is loaded when the scheduler runs a process
(i.e., changes the state of the process from ready to running). This is what I
(and I would guess you) did for the (processor) scheduling lab.

#### Accounting

At each tick, bump a counter in the process table entry for the currently
running process.

#### Alarm System Call and System Alarms

Users can request a signal at some future time (the Unix alarm system call).
The system also on occasion needs to schedule some of its own activities to
occur at specific times in the future (e.g., exercise a network time out).

The conceptually simplest solution is to have one timer for each event.
Instead, we simulate many timers with just one using the data structure on the
right with one node for each event.

![multiple-timers](http://cs.nyu.edu/~gottlieb/courses/os202/diagrams
/multiple-timers.png)

  * The first entry in each node is the time _after_ the preceding event that this event's alarm is to ring.
  * For example, if the time is zero, this event occurs at the same time as the previous event.
  * The second entry in the node is a pointer to the action to perform.
  * At each tick, the system decrements next-signal.
  * When next-signal goes to zero, we process the first entry on the list and any others immediately following with a time of zero (which means they are to be simultaneous with this alarm). We then set next-signal to the value in the next alarm.

#### Profiling

The objective is to obtain a histogram giving how much time was spent in each
software module of a given user program.

The program is logically divided into blocks of say 1KB and a counter is
associated with each block. At each tick the profiled code checks the program
counter and bumps the appropriate counter.

After the program is run, a (user-mode) utility program can determine the
software module associated with each 1K block and present the fraction of
execution time spent in each module.

If we use a finer granularity (say 10B instead of 1KB), we get increased
accuracy but more memory overhead.

**Homework:** 37\. The clock interrupt handler on a certain computer requires 2msec (including process switching overhead) per clock tick. The clock runs at 60 Hz. What fraction of the CPU is devoted to the clock.

### 5.5.3 Soft Timers

Skipped.

## 5.6 User Interfaces: Keyboard, Mouse, Monitor

### 5.6.2 Input Software

#### Keyboard Software

At each key press and key release a scan code is written into the keyboard
controller and the computer is interrupted. By remembering which keys have
been depressed and not released the software can determine Cntl-A, Shift-B,
etc.

There are two fundamental modes of input, traditionally called _raw_ and
_cooked_ in Unix and now sometimes called noncanonical and canonical in POSIX.
In raw mode the application sees every character the user types. Indeed, raw
mode is character oriented. All the OS does is convert the keyboard scan codes
to characters and and pass these characters to the application. For example

  1. down-cntl down-x up-x up-cntl is converted to cntl-x
  2. down-cntl up-cntl down-x up-x is converted to x
  3. down-cntl down-x up-cntl up-x is converted to cntl-x (I just tried it to be sure).
  4. down-x down-cntl up-x up-cntl is converted to x

Full screen editors use this mode.

Cooked mode is line oriented. The OS delivers lines to the application program
after cooking them as follows.

  * Special characters are interpreted as editing characters (erase-previous-character, erase-previous-word, kill-line, etc).
  * Erased characters are not seen by the application but are erased by the keyboard driver.
  * Also needed is an escape character so that the editing characters can be passed to the application if desired.
  * The cooked characters must be echoed (what should one do if the application is also generating output at this time?)

The (possibly cooked) characters must be buffered until the application issues
a read (and an end-of-line EOL has been received for cooked mode).

#### Mouse Software

Whenever the mouse is moved or a button is pressed, it sends a message to the
computer consisting of Δx, Δy, and the status of the buttons. That is all the
hardware does. Issues such as double click vs. two clicks are all handled by
the software.

### 5.6.3 Output Software

#### Text Windows

In the beginning these were essentially typewriters (called glass ttys) and
therefore simply received a stream of characters. Soon after, they accepted
commands (called escape sequences) that would position the cursor, insert and
delete characters, etc.

#### The X Window System

This is the window system on Unix machines. From the very beginning it was a
client-server system in which the server (the display manager) could run on a
separate machine from the clients (graphical applications such as pdf viewers,
calendars, browsers, etc).

#### Graphical User Interfaces (GUIs)

This is a large subject that would take many lectures to cover well. Both the
hardware and the software are complex. On a high-powered game computer, the
graphics hardware is more powerful and likely more expensive that the cpu on
which the operating system runs.

##### Bitmaps

  
  

##### Fonts

## 5.7 Thin Clients

## 5.8 Power Management

### 5.8.1 Hardware Issues

### 5.8.2 Operating System Issues

#### The Display

#### The Hard Disk

#### The CPU

#### The Memory

#### Wireless Communication

#### Thermal Management

#### Battery Management

#### Driver Interface

### Application Program Issues

## 5.9 Research on Input/Output

## 5.10 Summary

Read.

# The End: Good luck on the final!
