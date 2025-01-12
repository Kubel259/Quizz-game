class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
questions_answers_full = [
    {
        "question": "What is the key question posed in Alan Turing's paper 'Computing Machinery and Intelligence'?",
        "answer": "A",
        "A": "Can machines think?",
        "B": "How does the human mind work?",
        "C": "What is the future of AI?",
        "D": "Can humans become machines?",
        "E": "Are computers conscious?"
    },
    {
        "question": "What does the Chinese Room argument aim to challenge?",
        "answer": "B",
        "A": "The reliability of AI predictions.",
        "B": "The notion that AI can truly understand.",
        "C": "The ethical use of AI.",
        "D": "The speed of computation in AI.",
        "E": "The role of programming in AI development."
    },
    {
        "question": "According to Daniel Dennett, what is the purpose of the Turing Test?",
        "answer": "B",
        "A": "To measure AI's efficiency.",
        "B": "To test a machine's ability to exhibit intelligent behavior indistinguishable from a human.",
        "C": "To evaluate the speed of machine learning algorithms.",
        "D": "To explore the philosophical nature of consciousness.",
        "E": "To create human-like robots."
    },
    {
        "question": "In the Dartmouth Proposal of 1955, what was AI initially described as?",
        "answer": "B",
        "A": "The science of human-like computation.",
        "B": "The study of making machines use language and reason.",
        "C": "The automation of human emotions.",
        "D": "The development of military technology.",
        "E": "The exploration of neural networks."
    },
    {
        "question": "In Descartes' Meditation I, what is his main method for seeking knowledge?",
        "answer": "B",
        "A": "Trusting empirical evidence.",
        "B": "Systematic doubt.",
        "C": "Blind faith in God.",
        "D": "Dependence on mathematics.",
        "E": "Observational science."
    },
    {
        "question": "What philosophical concept does Descartes explore in the synopsis of Meditations?",
        "answer": "C",
        "A": "The immortality of the soul.",
        "B": "The separation of mind and body.",
        "C": "The reliability of sensory experiences.",
        "D": "The creation of an omniscient machine.",
        "E": "The existence of multiple realities."
    },
    {
        "question": "How does The Matrix illustrate Cartesian skepticism?",
        "answer": "B",
        "A": "By showing the relationship between humans and AI.",
        "B": "By questioning the reality of the perceived world.",
        "C": "By emphasizing the role of machines in the future.",
        "D": "By introducing a utopian society.",
        "E": "By explaining the origins of consciousness."
    },
    {
        "question": "What does 'Embodied' mean in 4E cognition?",
        "answer": "B",
        "A": "Cognition is tied to the brain only.",
        "B": "Cognition is influenced by the physical body.",
        "C": "Cognition is separate from the environment.",
        "D": "Cognition is purely symbolic.",
        "E": "Cognition is limited to cultural constructs."
    },
    {
        "question": "In 'Intelligence Without Representation,' Rodney Brooks argues that:",
        "answer": "B",
        "A": "AI must rely on symbolic representations.",
        "B": "Intelligence can emerge without pre-defined representations.",
        "C": "Neural networks are unnecessary.",
        "D": "Representations are the core of intelligence.",
        "E": "Machines cannot function without human input."
    },
    {
        "question": "What central claim does Alva Noë argue in Out of Our Heads?",
        "answer": "B",
        "A": "Consciousness is solely a product of the brain.",
        "B": "Consciousness arises from the interaction of brain, body, and environment.",
        "C": "Consciousness is an illusion created by neural activity.",
        "D": "Consciousness is tied to language development.",
        "E": "Consciousness is artificial in nature."
    },
    {
        "question": "What does Nick Bostrom identify as the key ethical issue in creating superintelligence?",
        "answer": "A",
        "A": "Ensuring human alignment in AI motivations.",
        "B": "Preventing technological growth.",
        "C": "Developing faster machines.",
        "D": "Limiting AI applications to entertainment.",
        "E": "Prioritizing AI over human concerns."
    },
    {
        "question": "What is a potential risk of the intelligence explosion, as discussed by Vernor Vinge?",
        "answer": "B",
        "A": "Machines will replace all humans in labor.",
        "B": "Superintelligence will have goals misaligned with human values.",
        "C": "AI will become slower as it grows.",
        "D": "Society will revert to primitive technology.",
        "E": "AI will focus solely on ethical behavior."
    },
    {
        "question": "What is the purpose of the Mirror Test in cognitive science?",
        "answer": "A",
        "A": "To measure self-awareness in animals.",
        "B": "To determine machine consciousness.",
        "C": "To assess visual perception in AI.",
        "D": "To explore human creativity.",
        "E": "To analyze decision-making in humans."
    },
    {
        "question": "According to Rebecca Saxe's TED Talk, what brain region is associated with understanding others' thoughts?",
        "answer": "B",
        "A": "The occipital lobe.",
        "B": "The temporo-parietal junction (TPJ).",
        "C": "The cerebellum.",
        "D": "The amygdala.",
        "E": "The frontal lobe."
    },
    {
        "question": "What is Richard Sutton's 'Bitter Lesson'?",
        "answer": "B",
        "A": "Human intuition is better than computation.",
        "B": "General computation scales better than handcrafted knowledge.",
        "C": "Symbolic AI will always outperform machine learning.",
        "D": "Supervised learning is the only valid approach.",
        "E": "Neural networks have reached their limit."
    },
    {
        "question": "What does the Turing Test assess?",
        "answer": "D",
        "A": "A machine's ability to write poetry.",
        "B": "A machine's ability to learn new skills autonomously.",
        "C": "A machine's ability to generate random responses.",
        "D": "A machine's ability to exhibit human-like intelligence.",
        "E": "A machine's speed in solving equations."
    },
    {
        "question": "According to John Searle's Chinese Room argument, what does a computer lack despite executing a program?",
        "answer": "C",
        "A": "Speed.",
        "B": "Syntax.",
        "C": "Understanding.",
        "D": "Accuracy.",
        "E": "Storage."
    },
    {
        "question": "What year was the Dartmouth Proposal, which marked the formal beginning of AI research, drafted?",
        "answer": "B",
        "A": "1945.",
        "B": "1955.",
        "C": "1965.",
        "D": "1975.",
        "E": "1985."
    },
    {
        "question": "In Meditation I, what does Descartes use the 'evil demon' thought experiment to illustrate?",
        "answer": "B",
        "A": "The existence of God.",
        "B": "The possibility that all sensory experiences could be deceptive.",
        "C": "The reliability of scientific knowledge.",
        "D": "The importance of moral behavior.",
        "E": "The superiority of mathematical reasoning."
    },
    {
        "question": "How does Descartes begin his argument in Meditations?",
        "answer": "B",
        "A": "By affirming the truth of sensory experiences.",
        "B": "By doubting everything he previously believed to be true.",
        "C": "By seeking empirical evidence for the existence of the world.",
        "D": "By analyzing the concept of causation.",
        "E": "By proving the immortality of the soul."
    },
    {
        "question": "In The Matrix, what is the role of the red pill, philosophically speaking?",
        "answer": "B",
        "A": "It symbolizes conformity to societal norms.",
        "B": "It represents the willingness to confront uncomfortable truths about reality.",
        "C": "It enhances one's physical abilities.",
        "D": "It eliminates emotional responses.",
        "E": "It allows the user to control the simulation."
    },
    {
        "question": "According to 4E Cognition, what does 'Extended' mean?",
        "answer": "B",
        "A": "Cognitive processes are limited to the brain.",
        "B": "Cognitive processes can include tools and external resources like calculators.",
        "C": "Cognitive processes are unrelated to the environment.",
        "D": "Cognition is entirely physical.",
        "E": "Cognition requires symbolic representations."
    },
    {
        "question": "What is the critique of symbolic AI according to Rodney Brooks' 'Intelligence Without Representation'?",
        "answer": "C",
        "A": "Symbolic AI cannot function without human intervention.",
        "B": "Symbolic AI is too slow to solve real-world problems.",
        "C": "Symbolic AI focuses too much on pre-defined representations rather than adaptive behavior.",
        "D": "Symbolic AI relies too heavily on neural networks.",
        "E": "Symbolic AI is only effective in games like chess."
    },
    {
        "question": "Alva Noë's argument in Out of Our Heads aligns most closely with which framework?",
        "answer": "C",
        "A": "Symbolic AI.",
        "B": "Cartesian skepticism.",
        "C": "4E Cognition.",
        "D": "The Turing Test.",
        "E": "Neural networks."
    },
    {
        "question": "What is a primary ethical concern in developing superintelligence, as noted by Nick Bostrom?",
        "answer": "C",
        "A": "The economic cost of creating AI.",
        "B": "The environmental impact of AI.",
        "C": "Ensuring superintelligence acts in humanity's best interests.",
        "D": "Preventing AI from becoming autonomous.",
        "E": "Limiting AI research to narrow domains."
    },
    {
        "question": "What is the 'Paperclip Maximizer' thought experiment intended to illustrate?",
        "answer": "B",
        "A": "The creativity of AI systems.",
        "B": "The dangers of misaligned AI goals.",
        "C": "The ability of AI to innovate beyond human capabilities.",
        "D": "The ethical responsibility of AI developers.",
        "E": "The potential for AI to create wealth."
    },
    {
        "question": "According to Vernor Vinge, why is the Singularity unpredictable?",
        "answer": "B",
        "A": "AI systems will resist development.",
        "B": "Superintelligence will evolve beyond human understanding.",
        "C": "Neural networks are inherently unstable.",
        "D": "AI will always require human oversight.",
        "E": "Computational power limits future progress."
    },
    {
        "question": "What does Rebecca Saxe suggest about understanding others' minds?",
        "answer": "B",
        "A": "It requires extensive logical reasoning.",
        "B": "It involves a specific brain region dedicated to social cognition.",
        "C": "It is impossible to achieve without verbal communication.",
        "D": "It depends entirely on cultural factors.",
        "E": "It is a purely instinctive process."
    },
    {
        "question": "What is the primary feature tested in the 'Mirror Test'?",
        "answer": "B",
        "A": "Memory retention.",
        "B": "Self-recognition and awareness.",
        "C": "Language development.",
        "D": "Problem-solving skills.",
        "E": "Visual acuity."
    },
    {
        "question": "According to Creativity in a Nutshell, what plays a crucial role in fostering creativity?",
        "answer": "B",
        "A": "High levels of intelligence.",
        "B": "Collaborative environments and divergent thinking.",
        "C": "Computational power.",
        "D": "Standardized testing.",
        "E": "Mastery of technical skills."
    },
    {
        "question": "What does Stuart Russell and Peter Norvig's definition of AI include?",
        "answer": "A",
        "A": "Machines that act rationally and think humanly.",
        "B": "Machines that only simulate emotions.",
        "C": "Machines that predict human behavior perfectly.",
        "D": "Machines that always follow ethical guidelines.",
        "E": "Machines that replace human labor entirely."
    },
    {
        "question": "What is the significance of the Dartmouth Conference (1955)?",
        "answer": "A",
        "A": "It introduced the term 'artificial intelligence.'",
        "B": "It launched the first neural network.",
        "C": "It developed the first AI ethical guidelines.",
        "D": "It standardized machine learning algorithms.",
        "E": "It created the Turing Test."
    },
    {
        "question": "What does John Searle’s 'syntax vs. semantics' argument imply?",
        "answer": "B",
        "A": "AI can fully replicate human thought.",
        "B": "AI processes symbols but lacks true understanding.",
        "C": "AI is incapable of solving mathematical problems.",
        "D": "AI has moral reasoning abilities.",
        "E": "AI relies solely on physical representation."
    },
    {
        "question": "What is the ultimate goal of Descartes' method of doubt?",
        "answer": "B",
        "A": "To question religious beliefs.",
        "B": "To establish a foundation for certain knowledge.",
        "C": "To disprove scientific theories.",
        "D": "To understand the nature of God.",
        "E": "To create a framework for ethics."
    },
    {
        "question": "In Meditations, what does Descartes conclude about his own existence?",
        "answer": "B",
        "A": "He is a physical being only.",
        "B": "He exists because he can doubt.",
        "C": "He exists because others perceive him.",
        "D": "He exists through empirical evidence.",
        "E": "He exists as a collection of sensory inputs."
    },
    {
        "question": "In The Matrix, what philosophical thought experiment does the simulation most closely resemble?",
        "answer": "B",
        "A": "Pascal's wager.",
        "B": "Brain in a vat.",
        "C": "Mind-body dualism.",
        "D": "The Ship of Theseus.",
        "E": "Occam's Razor."
    },
    {
        "question": "Which theorist introduced the idea of 4E cognition?",
        "answer": "B",
        "A": "Rodney Brooks.",
        "B": "James Carney.",
        "C": "Alan Turing.",
        "D": "Stuart Russell.",
        "E": "Nick Bostrom."
    },
    {
        "question": "How does 4E cognition differ from traditional views of cognition?",
        "answer": "B",
        "A": "It focuses on symbolic manipulation inside the brain.",
        "B": "It emphasizes the dynamic interaction of brain, body, and environment.",
        "C": "It limits cognition to biological processes.",
        "D": "It relies solely on computational models.",
        "E": "It suggests cognition is irrelevant to action."
    },
    {
        "question": "What is Rodney Brooks’ key critique of traditional AI?",
        "answer": "B",
        "A": "It is too focused on robotics.",
        "B": "It overemphasizes representation instead of behavior.",
        "C": "It ignores emotional intelligence.",
        "D": "It underestimates computational power.",
        "E": "It prioritizes ethics over efficiency."
    },
    {
        "question": "What does 'Embedded' mean in 4E cognition?",
        "answer": "B",
        "A": "Cognition involves adapting to cultural norms.",
        "B": "Cognition is affected by interactions with the environment.",
        "C": "Cognition is purely based on internal processes.",
        "D": "Cognition is limited to visual perception.",
        "E": "Cognition is independent of physical surroundings."
    },
    {
        "question": "What is a major concern highlighted in the Obermeyer et al. study on algorithms?",
        "answer": "B",
        "A": "The inability of AI to handle large datasets.",
        "B": "The potential for racial bias in algorithmic decision-making.",
        "C": "The slow progress in developing AI for healthcare.",
        "D": "The high cost of implementing AI systems.",
        "E": "The ethical challenges of using neural networks."
    },
    {
        "question": "Why does Nick Bostrom argue that AI motivations must be carefully designed?",
        "answer": "B",
        "A": "To ensure AI can adapt to various industries.",
        "B": "To prevent superintelligence from harming humanity.",
        "C": "To accelerate technological progress.",
        "D": "To align AI goals with corporate profit.",
        "E": "To limit AI to narrow applications."
    },
    {
        "question": "Which concept does the 'Paperclip Maximizer' illustrate?",
        "answer": "B",
        "A": "The scalability of AI systems.",
        "B": "The alignment problem in AI development.",
        "C": "The potential of AI in manufacturing.",
        "D": "The ethical implications of labor automation.",
        "E": "The limits of computational power."
    },
    {
        "question": "According to Vernor Vinge, what is a hallmark of superintelligence?",
        "answer": "A",
        "A": "Its ability to process data faster than any human.",
        "B": "Its potential to redefine human goals.",
        "C": "Its exclusive reliance on neural networks.",
        "D": "Its dependence on symbolic representations.",
        "E": "Its role in automating routine tasks."
    },
    {
        "question": "What does the Theory of Mind enable an entity to do?",
        "answer": "B",
        "A": "Solve complex equations.",
        "B": "Understand that others have thoughts and feelings.",
        "C": "Predict physical outcomes of actions.",
        "D": "Identify patterns in large datasets.",
        "E": "Communicate using verbal language."
    },
    {
        "question": "Why is creativity considered a core aspect of human intelligence?",
        "answer": "B",
        "A": "It is unique to human cognition.",
        "B": "It enables problem-solving and innovation.",
        "C": "It depends entirely on cultural upbringing.",
        "D": "It requires advanced mathematical reasoning.",
        "E": "It cannot be replicated by machines."
    },
    {
        "question": "In Rebecca Saxe's TED Talk, what method is used to study Theory of Mind?",
        "answer": "B",
        "A": "Behavioral experiments.",
        "B": "fMRI scans.",
        "C": "Neural simulations.",
        "D": "Computational models.",
        "E": "Philosophical thought experiments."
    },
    {
        "question": "What is the key lesson Richard Sutton emphasizes for AI progress?",
        "answer": "B",
        "A": "Human intuition should guide AI design.",
        "B": "General computation outperforms handcrafted knowledge.",
        "C": "Symbolic AI is the foundation of all advancements.",
        "D": "AI development requires minimal data.",
        "E": "Ethical considerations must always come first."
    },
    {
        "question": "Why does Sutton believe handcrafted solutions are limited?",
        "answer": "B",
        "A": "They require constant human intervention.",
        "B": "They do not scale as effectively as general methods.",
        "C": "They are only applicable to narrow domains.",
        "D": "They rely on outdated computational models.",
        "E": "They cannot adapt to new technologies."
    },
    {
        "question": "What does 'The Bitter Lesson' imply for AI researchers?",
        "answer": "B",
        "A": "Focus on specific tasks rather than general solutions.",
        "B": "Emphasize scalable computation over custom designs.",
        "C": "Prioritize neural network development.",
        "D": "Reject computational theories.",
        "E": "Use manual programming exclusively."
    },
    {
        "question": "What does Alan Turing suggest in his imitation game?",
        "answer": "B",
        "A": "Machines cannot think.",
        "B": "Machines can be indistinguishable from humans in specific tasks.",
        "C": "Human intelligence cannot be simulated.",
        "D": "Machines cannot learn.",
        "E": "Machines will always rely on human oversight."
    },
    {
        "question": "Which feature is critical in the Turing Test?",
        "answer": "A",
        "A": "The ability to deceive a human evaluator.",
        "B": "The speed of a machine's computation.",
        "C": "The ethical behavior of the machine.",
        "D": "The machine’s sensory capabilities.",
        "E": "The machine's physical resemblance to humans."
    },
    {
        "question": "Why does John Searle argue that a computer passing the Turing Test is insufficient proof of intelligence?",
        "answer": "B",
        "A": "Because computers cannot perform complex tasks.",
        "B": "Because the test measures external behavior, not understanding.",
        "C": "Because humans are biased evaluators.",
        "D": "Because computers rely on neural networks.",
        "E": "Because intelligence requires consciousness."
    },
    {
        "question": "In Meditations, what does Descartes conclude about the senses?",
        "answer": "B",
        "A": "They are the foundation of all knowledge.",
        "B": "They are unreliable for obtaining certain truth.",
        "C": "They provide a direct connection to reality.",
        "D": "They are a gift from God.",
        "E": "They should be trusted in scientific research."
    },
    {
        "question": "What does the phrase 'I think, therefore I am' (Cogito, ergo sum) signify?",
        "answer": "B",
        "A": "Existence is an illusion.",
        "B": "Doubt confirms the existence of a thinking self.",
        "C": "Thinking guarantees sensory accuracy.",
        "D": "Existence depends on God's will.",
        "E": "Thinking leads to physical reality."
    },
    {
        "question": "In the context of The Matrix, what does the simulation challenge?",
        "answer": "B",
        "A": "The reliability of technology.",
        "B": "The distinction between reality and illusion.",
        "C": "The potential of AI to become conscious.",
        "D": "The role of morality in AI systems.",
        "E": "The purpose of human existence."
    },
    {
        "question": "In 4E cognition, what role does 'Enacted' cognition play?",
        "answer": "A",
        "A": "It emphasizes cognition through interaction with the environment.",
        "B": "It limits cognition to internal processes.",
        "C": "It focuses on cultural knowledge.",
        "D": "It highlights cognitive development in children.",
        "E": "It excludes physical actions from cognition."
    },
    {
        "question": "How does 4E cognition describe the use of tools like calculators?",
        "answer": "B",
        "A": "They are part of embodied cognition.",
        "B": "They are examples of embedded or extended cognition.",
        "C": "They are irrelevant to cognitive processes.",
        "D": "They hinder creativity.",
        "E": "They belong to symbolic cognition."
    },
    {
        "question": "What is the primary critique of representation-heavy AI in Brooks’ work?",
        "answer": "B",
        "A": "It is too reliant on neural networks.",
        "B": "It lacks adaptability to real-world environments.",
        "C": "It prioritizes speed over accuracy.",
        "D": "It cannot process large datasets.",
        "E": "It is incompatible with machine learning."
    },
    {
        "question": "What is the primary objective of AI alignment, as discussed by Nick Bostrom?",
        "answer": "B",
        "A": "To maximize computational efficiency.",
        "B": "To ensure AI goals align with human values.",
        "C": "To increase AI’s autonomy.",
        "D": "To limit AI applications to research.",
        "E": "To prioritize corporate interests in AI development."
    },
    {
        "question": "What does Vernor Vinge's 'intelligence explosion' refer to?",
        "answer": "B",
        "A": "AI systems developing sentience.",
        "B": "Rapid self-improvement of superintelligence.",
        "C": "AI outcompeting humans in all fields.",
        "D": "Neural networks dominating AI research.",
        "E": "Machines replacing human labor worldwide."
    },
    {
        "question": "Why is 'value misalignment' a key ethical risk in AI?",
        "answer": "B",
        "A": "AI systems might overestimate their capabilities.",
        "B": "AI systems could pursue goals harmful to humans.",
        "C": "AI systems cannot handle ambiguous instructions.",
        "D": "AI systems will reject moral guidelines.",
        "E": "AI systems lack computational power for ethics."
    },
    {
        "question": "What is one key characteristic of Theory of Mind?",
        "answer": "B",
        "A": "It involves memory retention.",
        "B": "It requires understanding others' beliefs and emotions.",
        "C": "It is limited to visual recognition tasks.",
        "D": "It excludes linguistic understanding.",
        "E": "It is unique to humans."
    },
    {
        "question": "In Rebecca Saxe's work, how is Theory of Mind studied?",
        "answer": "B",
        "A": "Through behavioral observations only.",
        "B": "Using neuroimaging techniques like fMRI.",
        "C": "By simulating cognition in robots.",
        "D": "Through philosophical debates.",
        "E": "By analyzing AI decision-making processes."
    },
    {
        "question": "What does Creativity in a Nutshell suggest as a requirement for creativity?",
        "answer": "B",
        "A": "Strict adherence to rules.",
        "B": "Collaboration and divergent thinking.",
        "C": "Isolation from external influences.",
        "D": "Mastery of advanced mathematics.",
        "E": "Reliance on symbolic representations."
    },
    {
        "question": "What key message does 'The Bitter Lesson' emphasize for AI research?",
        "answer": "B",
        "A": "Focus on handcrafted solutions.",
        "B": "Leverage general methods that scale well with computation.",
        "C": "Prioritize symbolic approaches over neural networks.",
        "D": "Limit the role of data in AI systems.",
        "E": "Emphasize human intuition in AI design."
    },
    {
        "question": "Why does Richard Sutton argue against handcrafted solutions?",
        "answer": "B",
        "A": "They are too computationally expensive.",
        "B": "They fail to generalize across diverse tasks.",
        "C": "They are not compatible with ethical frameworks.",
        "D": "They rely on outdated programming models.",
        "E": "They are too data-intensive."
    },
    {
        "question": "What does Sutton suggest is the driving force behind AI's progress?",
        "answer": "B",
        "A": "Human creativity.",
        "B": "Scalable computation.",
        "C": "Handcrafted expertise.",
        "D": "Symbolic reasoning.",
        "E": "Minimal data usage."
    },
    {
        "question": "In Turing's paper, why does he propose replacing the question 'Can machines think?' with the 'imitation game'?",
        "answer": "B",
        "A": "To simplify the philosophical debate.",
        "B": "To provide a measurable and practical test for machine intelligence.",
        "C": "To highlight human biases in AI evaluation.",
        "D": "To avoid focusing on biological comparisons.",
        "E": "To emphasize computational speed."
    },
    {
        "question": "Which of the following best describes the Chinese Room argument?",
        "answer": "B",
        "A": "A demonstration of a machine's ability to understand language.",
        "B": "A critique of the idea that symbol manipulation equals understanding.",
        "C": "A defense of AI as a form of conscious thought.",
        "D": "An argument supporting the superiority of neural networks.",
        "E": "A philosophical discussion on ethics in AI."
    },
    {
        "question": "What does the Dartmouth Proposal emphasize as a goal of AI research?",
        "answer": "B",
        "A": "To create machines that can play chess.",
        "B": "To simulate every aspect of human intelligence.",
        "C": "To eliminate the need for human intervention in decision-making.",
        "D": "To design robots that replace human labor.",
        "E": "To integrate ethical guidelines into AI systems."
    },
    {
        "question": "In Meditation I, why does Descartes question the reliability of mathematics?",
        "answer": "B",
        "A": "He believes mathematical truths are dependent on sensory experience.",
        "B": "He considers the possibility of a deceptive God or demon influencing his reasoning.",
        "C": "He rejects mathematics as a valid form of knowledge.",
        "D": "He finds errors in mathematical proofs.",
        "E": "He views mathematics as inferior to empirical sciences."
    },
    {
        "question": "According to Descartes, what can he be certain of in Meditation I?",
        "answer": "B",
        "A": "The existence of the physical world.",
        "B": "The existence of his own thoughts.",
        "C": "The reliability of his senses.",
        "D": "The infallibility of mathematics.",
        "E": "The presence of other conscious beings."
    },
    {
        "question": "How does The Matrix explore themes of epistemology?",
        "answer": "B",
        "A": "By focusing on ethical dilemmas.",
        "B": "By illustrating how knowledge can be deceptive in a simulated reality.",
        "C": "By emphasizing the role of technology in improving intelligence.",
        "D": "By showing the dangers of AI control over society.",
        "E": "By examining the impact of virtual worlds on human interaction."
    },
    {
        "question": "What does 'Embodied' cognition imply about human thought processes?",
        "answer": "B",
        "A": "They are purely symbolic and abstract.",
        "B": "They are shaped by the body’s interactions with the world.",
        "C": "They are unaffected by physical limitations.",
        "D": "They rely on linguistic structures.",
        "E": "They are entirely determined by genetics."
    },
    {
        "question": "Why is 'Extended' cognition significant in 4E cognition theory?",
        "answer": "B",
        "A": "It suggests cognition is static.",
        "B": "It emphasizes the use of tools and external systems as part of cognitive processes.",
        "C": "It rejects the role of culture in cognition.",
        "D": "It limits cognition to neural activity.",
        "E": "It denies the role of emotions in cognition."
    },
    {
        "question": "In Brooks’ work, why is representation seen as unnecessary for certain forms of intelligence?",
        "answer": "B",
        "A": "Representation adds computational complexity.",
        "B": "Adaptive behavior can emerge from direct interaction with the environment.",
        "C": "Representation is outdated for modern AI systems.",
        "D": "Representation depends solely on symbolic reasoning.",
        "E": "Representation works only for narrow AI tasks."
    },
    {
        "question": "What ethical principle is central to Bostrom's work on superintelligence?",
        "answer": "B",
        "A": "Ensuring AI autonomy.",
        "B": "Designing AI systems with human-friendly motivations.",
        "C": "Prioritizing computational efficiency over ethical concerns.",
        "D": "Using AI for military advancements.",
        "E": "Accelerating AI development at any cost."
    },
    {
        "question": "According to the 'intelligence explosion,' what happens once superintelligence emerges?",
        "answer": "B",
        "A": "It halts human progress.",
        "B": "It rapidly self-improves, leading to exponential advancements.",
        "C": "It becomes entirely dependent on human input.",
        "D": "It is limited by computational power.",
        "E": "It focuses on a single domain."
    },
    {
        "question": "What does Obermeyer et al.'s study reveal about AI systems?",
        "answer": "B",
        "A": "AI systems eliminate all forms of bias.",
        "B": "AI systems can perpetuate existing racial biases in healthcare algorithms.",
        "C": "AI systems are always neutral in decision-making.",
        "D": "AI systems are immune to cultural influences.",
        "E": "AI systems cannot handle complex data."
    },
    {
        "question": "What is one key indicator of Theory of Mind in humans and animals?",
        "answer": "B",
        "A": "The ability to mimic behaviors.",
        "B": "The ability to understand that others have beliefs different from their own.",
        "C": "The ability to solve complex mathematical problems.",
        "D": "The ability to create language.",
        "E": "The ability to recall memories."
    },
    {
        "question": "In creativity research, what role does divergent thinking play?",
        "answer": "B",
        "A": "It limits creative potential.",
        "B": "It generates multiple solutions to a problem.",
        "C": "It enforces strict rules for innovation.",
        "D": "It focuses solely on logical problem-solving.",
        "E": "It prevents collaboration."
    },
    {
        "question": "How does Rebecca Saxe link Theory of Mind to brain activity?",
        "answer": "B",
        "A": "She shows that it is unrelated to neural activity.",
        "B": "She identifies the temporo-parietal junction as critical for understanding others' thoughts.",
        "C": "She demonstrates its reliance on the frontal cortex alone.",
        "D": "She links it exclusively to memory regions.",
        "E": "She argues it is purely instinctive."
    },
    {
        "question": "Why does Sutton advocate for general methods over handcrafted solutions?",
        "answer": "B",
        "A": "General methods rely less on computational power.",
        "B": "General methods scale better with increasing data and computation.",
        "C": "Handcrafted solutions are faster to implement.",
        "D": "Handcrafted solutions guarantee better performance.",
        "E": "Handcrafted solutions are more ethical."
    },
    {
        "question": "What is a practical implication of 'The Bitter Lesson' for AI development?",
        "answer": "B",
        "A": "Avoid investing in neural networks.",
        "B": "Focus on scalable learning techniques.",
        "C": "Prioritize domain-specific programming.",
        "D": "Reduce reliance on computational power.",
        "E": "Use pre-programmed heuristics exclusively."
    },
    {
        "question": "In Turing’s 'Computing Machinery and Intelligence,' what is a key feature of the imitation game?",
        "answer": "B",
        "A": "It involves physical interaction between the interrogator and the machine.",
        "B": "The interrogator must determine which is the machine through textual communication.",
        "C": "It tests the machine's ability to perform calculations quickly.",
        "D": "It requires the machine to mimic human emotions.",
        "E": "It focuses on the machine's ethical decision-making."
    },
    {
        "question": "What does the 'Chinese Room' argument demonstrate about AI?",
        "answer": "B",
        "A": "AI cannot perform complex computations.",
        "B": "AI lacks understanding, even when it simulates intelligent behavior.",
        "C": "AI can understand language like humans.",
        "D": "AI surpasses human intelligence in decision-making.",
        "E": "AI is inherently ethical."
    },
    {
        "question": "According to the Dartmouth Proposal, which is a key aspect of AI research?",
        "answer": "A",
        "A": "Building machines that can learn from experience.",
        "B": "Programming machines to follow strict rules.",
        "C": "Simulating physical movements of humans.",
        "D": "Creating ethical guidelines for machine behavior.",
        "E": "Limiting AI research to mathematical problems."
    },
    {
        "question": "How does Descartes distinguish between dreaming and waking reality in Meditation I?",
        "answer": "B",
        "A": "By relying on sensory evidence.",
        "B": "By questioning the clarity and distinctness of his perceptions.",
        "C": "By analyzing the consistency of dreams.",
        "D": "By rejecting all sensory inputs.",
        "E": "By focusing on mathematical truths."
    },
    {
        "question": "What role does the 'evil demon' play in Descartes’ method of doubt?",
        "answer": "B",
        "A": "It illustrates the certainty of divine existence.",
        "B": "It serves as a hypothetical being that deceives his senses.",
        "C": "It disproves the reliability of mathematics.",
        "D": "It confirms the trustworthiness of his mind.",
        "E": "It emphasizes the importance of sensory data."
    },
    {
        "question": "In The Matrix, why is Neo’s journey significant to Cartesian skepticism?",
        "answer": "B",
        "A": "It shows that knowledge is based on empirical evidence.",
        "B": "It illustrates how one can doubt reality and seek foundational truth.",
        "C": "It proves the reliability of sensory perception.",
        "D": "It emphasizes the power of artificial intelligence.",
        "E": "It demonstrates the value of collective consciousness."
    },
    {
        "question": "What does 'Enacted' cognition emphasize?",
        "answer": "B",
        "A": "The role of cultural norms in shaping thought.",
        "B": "The idea that cognition involves action and interaction with the environment.",
        "C": "The reliance on symbolic representation.",
        "D": "The limitation of cognition to biological processes.",
        "E": "The rejection of external influences in cognition."
    },
    {
        "question": "In 4E Cognition, why is the use of tools considered 'Extended' cognition?",
        "answer": "B",
        "A": "Tools replace cognitive processes.",
        "B": "Tools function as external resources that enhance cognitive tasks.",
        "C": "Tools simplify symbolic representation.",
        "D": "Tools are part of human memory systems.",
        "E": "Tools limit cognitive flexibility."
    },
    {
        "question": "How does Rodney Brooks’ critique of traditional AI relate to real-world behavior?",
        "answer": "A",
        "A": "Traditional AI focuses on abstract reasoning rather than adaptive action.",
        "B": "Traditional AI relies too much on neural networks.",
        "C": "Traditional AI overemphasizes physical embodiment.",
        "D": "Traditional AI is more effective in dynamic environments.",
        "E": "Traditional AI surpasses machine learning in adaptability."
    },
    {
        "question": "What is Nick Bostrom’s primary recommendation for creating superintelligence?",
        "answer": "B",
        "A": "To limit superintelligence to narrow applications.",
        "B": "To align its motivations with human-friendly goals.",
        "C": "To enhance its computational power.",
        "D": "To prevent its creation entirely.",
        "E": "To prioritize military applications."
    },
    {
        "question": "What is the 'alignment problem' in AI ethics?",
        "answer": "C",
        "A": "Ensuring AI processes large datasets efficiently.",
        "B": "Preventing AI from developing its own goals.",
        "C": "Aligning AI goals and behaviors with human values.",
        "D": "Enhancing the computational speed of AI systems.",
        "E": "Creating AI systems that are entirely autonomous."
    },
    {
        "question": "According to Vernor Vinge, what could be a risk of superintelligence?",
        "answer": "B",
        "A": "It will fail to process data efficiently.",
        "B": "It could become uncontrollable and pursue goals misaligned with human values.",
        "C": "It will always require human supervision.",
        "D": "It will cease improving after a certain threshold.",
        "E": "It will lack decision-making capabilities."
    },
    {
        "question": "What does Rebecca Saxe identify as crucial for understanding others' intentions?",
        "answer": "B",
        "A": "Emotional intelligence.",
        "B": "The temporo-parietal junction in the brain.",
        "C": "Logical reasoning abilities.",
        "D": "Cultural upbringing.",
        "E": "Instinctive behavior."
    },
    {
        "question": "Why is the Mirror Test significant in understanding self-awareness?",
        "answer": "B",
        "A": "It assesses an individual’s memory.",
        "B": "It determines the ability to recognize oneself in a reflection.",
        "C": "It evaluates social interaction skills.",
        "D": "It measures intelligence quotient (IQ).",
        "E": "It tests problem-solving abilities."
    },
    {
        "question": "What does Creativity in a Nutshell argue about collaborative environments?",
        "answer": "B",
        "A": "They limit the potential for original ideas.",
        "B": "They enhance creativity through shared perspectives.",
        "C": "They hinder divergent thinking.",
        "D": "They prioritize individual achievements.",
        "E": "They are unnecessary for fostering innovation."
    }
]

