import pygame
import random, difflib, time, sys

pygame.init()
currenttime = 0
timepress = 0
z = 0
text2 = ''
tester = 0
counter = 0
counter1 = ''
tdifference = 0
gametimer = 0
accuracy = '0'
tchar = 0
enterbutton = 1
spacebutton = 0
wpm = 0
seconds = 0

thewords = ["a", "abandon", "ability", "able", "abortion", "about", "above", "abroad", "absence", "absolute",
            "absolutely",
            "absorb", "abuse", "academic", "accept", "access", "accident", "accompany", "accomplish", "according",
            "account", "accurate", "accuse", "achieve", "achievement", "acid", "acknowledge", "acquire", "across",
            "act",
            "action", "active", "activist", "activity", "actor", "actress", "actual", "actually", "ad", "adapt", "add",
            "addition", "additional", "address", "adequate", "adjust", "adjustment", "administration", "administrator",
            "admire", "admission", "admit", "adolescent", "adopt", "adult", "advance", "advanced", "advantage",
            "adventure", "advertising", "advice", "advise", "adviser", "advocate", "affair", "affect", "afford",
            "afraid",
            "African", "African-American", "after", "afternoon", "again", "against", "age", "agency", "agenda", "agent",
            "aggressive", "ago", "agree", "agreement", "agricultural", "ah", "ahead", "aid", "aide", "AIDS", "aim",
            "air",
            "aircraft", "airline", "airport", "album", "alcohol", "alive", "all", "alliance", "allow", "ally", "almost",
            "alone", "along", "already", "also", "alter", "alternative", "although", "always", "AM", "amazing",
            "American",
            "among", "amount", "analysis", "analyst", "analyze", "ancient", "and", "anger", "angle", "angry", "animal",
            "anniversary", "announce", "annual", "another", "answer", "anticipate", "anxiety", "any", "anybody",
            "anymore",
            "anyone", "anything", "anyway", "anywhere", "apart", "apartment", "apparent", "apparently", "appeal",
            "appear",
            "appearance", "apple", "application", "apply", "appoint", "appointment", "appreciate", "approach",
            "appropriate", "approval", "approve", "approximately", "Arab", "architect", "area", "argue", "argument",
            "arise", "arm", "armed", "army", "around", "arrange", "arrangement", "arrest", "arrival", "arrive", "art",
            "article", "artist", "artistic", "as", "Asian", "aside", "ask", "asleep", "aspect", "assault", "assert",
            "assess", "assessment", "asset", "assign", "assignment", "assist", "assistance", "assistant", "associate",
            "association", "assume", "assumption", "assure", "at", "athlete", "athletic", "atmosphere", "attach",
            "attack",
            "attempt", "attend", "attention", "attitude", "attorney", "attract", "attractive", "attribute", "audience",
            "author", "authority", "auto", "available", "average", "avoid", "award", "aware", "awareness", "away",
            "awful",
            "baby", "back", "background", "bad", "badly", "bag", "bake", "balance", "ball", "ban", "band", "bank",
            "bar",
            "barely", "barrel", "barrier", "base", "baseball", "basic", "basically", "basis", "basket", "basketball",
            "bathroom", "battery", "battle", "be", "beach", "bean", "bear", "beat", "beautiful", "beauty", "because",
            "become", "bed", "bedroom", "beer", "before", "begin", "beginning", "behavior", "behind", "being", "belief",
            "believe", "bell", "belong", "below", "belt", "bench", "bend", "beneath", "benefit", "beside", "besides",
            "best", "bet", "better", "between", "beyond", "Bible", "big", "bike", "bill", "billion", "bind",
            "biological",
            "bird", "birth", "birthday", "bit", "bite", "black", "blade", "blame", "blanket", "blind", "block", "blood",
            "blow", "blue", "board", "boat", "body", "bomb", "bombing", "bond", "bone", "book", "boom", "boot",
            "border",
            "born", "borrow", "boss", "both", "bother", "bottle", "bottom", "boundary", "bowl", "box", "boy",
            "boyfriend",
            "brain", "branch", "brand", "bread", "break", "breakfast", "breast", "breath", "breathe", "brick", "bridge",
            "brief", "briefly", "bright", "brilliant", "bring", "British", "broad", "broken", "brother", "brown",
            "brush",
            "buck", "budget", "build", "building", "bullet", "bunch", "burden", "burn", "bury", "bus", "business",
            "busy",
            "but", "butter", "button", "buy", "buyer", "by", "cabin", "cabinet", "cable", "cake", "calculate", "call",
            "camera", "camp", "campaign", "campus", "can", "Canadian", "cancer", "candidate", "cap", "capability",
            "capable", "capacity", "capital", "captain", "capture", "car", "carbon", "card", "care", "career",
            "careful",
            "carefully", "carrier", "carry", "case", "cash", "cast", "cat", "catch", "category", "Catholic", "cause",
            "ceiling", "celebrate", "celebration", "celebrity", "cell", "center", "central", "century", "CEO",
            "ceremony",
            "certain", "certainly", "chain", "chair", "chairman", "challenge", "chamber", "champion", "championship",
            "chance", "change", "changing", "channel", "chapter", "character", "characteristic", "characterize",
            "charge",
            "charity", "chart", "chase", "cheap", "check", "cheek", "cheese", "chef", "chemical", "chest", "chicken",
            "chief", "child", "childhood", "Chinese", "chip", "chocolate", "choice", "cholesterol", "choose",
            "Christian",
            "Christmas", "church", "cigarette", "circle", "circumstance", "cite", "citizen", "city", "civil",
            "civilian",
            "claim", "class", "classic", "classroom", "clean", "clear", "clearly", "client", "climate", "climb",
            "clinic",
            "clinical", "clock", "close", "closely", "closer", "clothes", "clothing", "cloud", "club", "clue",
            "cluster",
            "coach", "coal", "coalition", "coast", "coat", "code", "coffee", "cognitive", "cold", "collapse",
            "colleague",
            "collect", "collection", "collective", "college", "colonial", "color", "column", "combination", "combine",
            "come", "comedy", "comfort", "comfortable", "command", "commander", "comment", "commercial", "commission",
            "commit", "commitment", "committee", "common", "communicate", "communication", "community", "company",
            "compare", "comparison", "compete", "competition", "competitive", "competitor", "complain", "complaint",
            "complete", "completely", "complex", "complicated", "component", "compose", "composition", "comprehensive",
            "computer", "concentrate", "concentration", "concept", "concern", "concerned", "concert", "conclude",
            "conclusion", "concrete", "condition", "conduct", "conference", "confidence", "confident", "confirm",
            "conflict", "confront", "confusion", "Congress", "congressional", "connect", "connection", "consciousness",
            "consensus", "consequence", "conservative", "consider", "considerable", "consideration", "consist",
            "consistent", "constant", "constantly", "constitute", "constitutional", "construct", "construction",
            "consultant", "consume", "consumer", "consumption", "contact", "contain", "container", "contemporary",
            "content", "contest", "context", "continue", "continued", "contract", "contrast", "contribute",
            "contribution",
            "control", "controversial", "controversy", "convention", "conventional", "conversation", "convert",
            "conviction", "convince", "cook", "cookie", "cooking", "cool", "cooperation", "cop", "cope", "copy", "core",
            "corn", "corner", "corporate", "corporation", "correct", "correspondent", "cost", "cotton", "couch",
            "could",
            "council", "counselor", "count", "counter", "country", "county", "couple", "courage", "course", "court",
            "cousin", "cover", "coverage", "cow", "crack", "craft", "crash", "crazy", "cream", "create", "creation",
            "creative", "creature", "credit", "crew", "crime", "criminal", "crisis", "criteria", "critic", "critical",
            "criticism", "criticize", "crop", "cross", "crowd", "crucial", "cry", "cultural", "culture", "cup",
            "curious",
            "current", "currently", "curriculum", "custom", "customer", "cut", "cycle", "dad", "daily", "damage",
            "dance",
            "danger", "dangerous", "dare", "dark", "darkness", "data", "date", "daughter", "day", "dead", "deal",
            "dealer",
            "dear", "death", "debate", "debt", "decade", "decide", "decision", "deck", "declare", "decline", "decrease",
            "deep", "deeply", "deer", "defeat", "defend", "defendant", "defense", "defensive", "deficit", "define",
            "definitely", "definition", "degree", "delay", "deliver", "delivery", "demand", "democracy", "Democrat",
            "democratic", "demonstrate", "demonstration", "deny", "department", "depend", "dependent", "depending",
            "depict", "depression", "depth", "deputy", "derive", "describe", "description", "desert", "deserve",
            "design",
            "designer", "desire", "desk", "desperate", "despite", "destroy", "destruction", "detail", "detailed",
            "detect",
            "determine", "develop", "developing", "development", "device", "devote", "dialogue", "die", "diet",
            "differ",
            "difference", "different", "differently", "difficult", "difficulty", "dig", "digital", "dimension",
            "dining",
            "dinner", "direct", "direction", "directly", "director", "dirt", "dirty", "disability", "disagree",
            "disappear", "disaster", "discipline", "discourse", "discover", "discovery", "discrimination", "discuss",
            "discussion", "disease", "dish", "dismiss", "disorder", "display", "dispute", "distance", "distant",
            "distinct", "distinction", "distinguish", "distribute", "distribution", "district", "diverse", "diversity",
            "divide", "division", "divorce", "DNA", "do", "doctor", "document", "dog", "domestic", "dominant",
            "dominate",
            "door", "double", "doubt", "down", "downtown", "dozen", "draft", "drag", "drama", "dramatic",
            "dramatically",
            "draw", "drawing", "dream", "dress", "drink", "drive", "driver", "drop", "drug", "dry", "due", "during",
            "dust", "duty", "each", "eager", "ear", "early", "earn", "earnings", "earth", "ease", "easily", "east",
            "eastern", "easy", "eat", "economic", "economics", "economist", "economy", "edge", "edition", "editor",
            "educate", "education", "educational", "educator", "effect", "effective", "effectively", "efficiency",
            "efficient", "effort", "egg", "eight", "either", "elderly", "elect", "election", "electric", "electricity",
            "electronic", "element", "elementary", "eliminate", "elite", "else", "elsewhere", "e-mail", "embrace",
            "emerge", "emergency", "emission", "emotion", "emotional", "emphasis", "emphasize", "employ", "employee",
            "employer", "employment", "empty", "enable", "encounter", "encourage", "end", "enemy", "energy",
            "enforcement",
            "engage", "engine", "engineer", "engineering", "English", "enhance", "enjoy", "enormous", "enough",
            "ensure",
            "enter", "enterprise", "entertainment", "entire", "entirely", "entrance", "entry", "environment",
            "environmental", "episode", "equal", "equally", "equipment", "era", "error", "escape", "especially",
            "essay",
            "essential", "essentially", "establish", "establishment", "estate", "estimate", "etc", "ethics", "ethnic",
            "European", "evaluate", "evaluation", "even", "evening", "event", "eventually", "ever", "every",
            "everybody",
            "everyday", "everyone", "everything", "everywhere", "evidence", "evolution", "evolve", "exact", "exactly",
            "examination", "examine", "example", "exceed", "excellent", "except", "exception", "exchange", "exciting",
            "executive", "exercise", "exhibit", "exhibition", "exist", "existence", "existing", "expand", "expansion",
            "expect", "expectation", "expense", "expensive", "experience", "experiment", "expert", "explain",
            "explanation", "explode", "explore", "explosion", "expose", "exposure", "express", "expression", "extend",
            "extension", "extensive", "extent", "external", "extra", "extraordinary", "extreme", "extremely", "eye",
            "fabric", "face", "facility", "fact", "factor", "factory", "faculty", "fade", "fail", "failure", "fair",
            "fairly", "faith", "fall", "FALSE", "familiar", "family", "famous", "fan", "fantasy", "far", "farm",
            "farmer",
            "fashion", "fast", "fat", "fate", "father", "fault", "favor", "favorite", "fear", "feature", "federal",
            "fee",
            "feed", "feel", "feeling", "fellow", "female", "fence", "few", "fewer", "fiber", "fiction", "field",
            "fifteen",
            "fifth", "fifty", "fight", "fighter", "fighting", "figure", "file", "fill", "film", "final", "finally",
            "finance", "financial", "find", "finding", "fine", "finger", "finish", "fire", "firm", "first", "fish",
            "fishing", "fit", "fitness", "five", "fix", "flag", "flame", "flat", "flavor", "flee", "flesh", "flight",
            "float", "floor", "flow", "flower", "fly", "focus", "folk", "follow", "following", "food", "foot",
            "football",
            "for", "force", "foreign", "forest", "forever", "forget", "form", "formal", "formation", "former",
            "formula",
            "forth", "fortune", "forward", "found", "foundation", "founder", "four", "fourth", "frame", "framework",
            "free", "freedom", "freeze", "French", "frequency", "frequent", "frequently", "fresh", "friend", "friendly",
            "friendship", "from", "front", "fruit", "frustration", "fuel", "full", "fully", "fun", "function", "fund",
            "fundamental", "funding", "funeral", "funny", "furniture", "furthermore", "future", "gain", "galaxy",
            "gallery", "game", "gang", "gap", "garage", "garden", "garlic", "gas", "gate", "gather", "gay", "gaze",
            "gear",
            "gender", "gene", "general", "generally", "generate", "generation", "genetic", "gentleman", "gently",
            "German",
            "gesture", "get", "ghost", "giant", "gift", "gifted", "girl", "girlfriend", "give", "given", "glad",
            "glance",
            "glass", "global", "glove", "go", "goal", "God", "gold", "golden", "golf", "good", "government", "governor",
            "grab", "grade", "gradually", "graduate", "grain", "grand", "grandfather", "grandmother", "grant", "grass",
            "grave", "gray", "great", "greatest", "green", "grocery", "ground", "group", "grow", "growing", "growth",
            "guarantee", "guard", "guess", "guest", "guide", "guideline", "guilty", "gun", "guy", "habit", "habitat",
            "hair", "half", "hall", "hand", "handful", "handle", "hang", "happen", "happy", "hard", "hardly", "hat",
            "hate", "have", "he", "head", "headline", "headquarters", "health", "healthy", "hear", "hearing", "heart",
            "heat", "heaven", "heavily", "heavy", "heel", "height", "helicopter", "hell", "hello", "help", "helpful",
            "her", "here", "heritage", "hero", "herself", "hey", "hi", "hide", "high", "highlight", "highly", "highway",
            "hill", "him", "himself", "hip", "hire", "his", "historian", "historic", "historical", "history", "hit",
            "hold", "hole", "holiday", "holy", "home", "homeless", "honest", "honey", "honor", "hope", "horizon",
            "horror",
            "horse", "hospital", "host", "hot", "hotel", "hour", "house", "household", "housing", "how", "however",
            "huge",
            "human", "humor", "hundred", "hungry", "hunter", "hunting", "hurt", "husband", "hypothesis", "I", "ice",
            "idea", "ideal", "identification", "identify", "identity", "ie", "if", "ignore", "ill", "illegal",
            "illness",
            "illustrate", "image", "imagination", "imagine", "immediate", "immediately", "immigrant", "immigration",
            "impact", "implement", "implication", "imply", "importance", "important", "impose", "impossible", "impress",
            "impression", "impressive", "improve", "improvement", "in", "incentive", "incident", "include", "including",
            "income", "incorporate", "increase", "increased", "increasing", "increasingly", "incredible", "indeed",
            "independence", "independent", "index", "Indian", "indicate", "indication", "individual", "industrial",
            "industry", "infant", "infection", "inflation", "influence", "inform", "information", "ingredient",
            "initial",
            "initially", "initiative", "injury", "inner", "innocent", "inquiry", "inside", "insight", "insist",
            "inspire",
            "install", "instance", "instead", "institution", "institutional", "instruction", "instructor", "instrument",
            "insurance", "intellectual", "intelligence", "intend", "intense", "intensity", "intention", "interaction",
            "interest", "interested", "interesting", "internal", "international", "Internet", "interpret",
            "interpretation", "intervention", "interview", "into", "introduce", "introduction", "invasion", "invest",
            "investigate", "investigation", "investigator", "investment", "investor", "invite", "involve", "involved",
            "involvement", "Iraqi", "Irish", "iron", "Islamic", "island", "Israeli", "issue", "it", "Italian", "item",
            "its", "itself", "jacket", "jail", "Japanese", "jet", "Jew", "Jewish", "job", "join", "joint", "joke",
            "journal", "journalist", "journey", "joy", "judge", "judgment", "juice", "jump", "junior", "jury", "just",
            "justice", "justify", "keep", "key", "kick", "kid", "kill", "killer", "killing", "kind", "king", "kiss",
            "kitchen", "knee", "knife", "knock", "know", "knowledge", "lab", "label", "labor", "laboratory", "lack",
            "lady", "lake", "land", "landscape", "language", "lap", "large", "largely", "last", "late", "later",
            "Latin",
            "latter", "laugh", "launch", "law", "lawn", "lawsuit", "lawyer", "lay", "layer", "lead", "leader",
            "leadership", "leading", "leaf", "league", "lean", "learn", "learning", "least", "leather", "leave", "left",
            "leg", "legacy", "legal", "legend", "legislation", "legitimate", "lemon", "length", "less", "lesson", "let",
            "letter", "level", "liberal", "library", "license", "lie", "life", "lifestyle", "lifetime", "lift", "light",
            "like", "likely", "limit", "limitation", "limited", "line", "link", "lip", "list", "listen", "literally",
            "literary", "literature", "little", "live", "living", "load", "loan", "local", "locate", "location", "lock",
            "long", "long-term", "look", "loose", "lose", "loss", "lost", "lot", "lots", "loud", "love", "lovely",
            "lover",
            "low", "lower", "luck", "lucky", "lunch", "lung", "machine", "mad", "magazine", "mail", "main", "mainly",
            "maintain", "maintenance", "major", "majority", "make", "maker", "makeup", "male", "mall", "man", "manage",
            "management", "manager", "manner", "manufacturer", "manufacturing", "many", "map", "margin", "mark",
            "market",
            "marketing", "marriage", "married", "marry", "mask", "mass", "massive", "master", "match", "material",
            "math",
            "matter", "may", "maybe", "mayor", "me", "meal", "mean", "meaning", "meanwhile", "measure", "measurement",
            "meat", "mechanism", "media", "medical", "medication", "medicine", "medium", "meet", "meeting", "member",
            "membership", "memory", "mental", "mention", "menu", "mere", "merely", "mess", "message", "metal", "meter",
            "method", "Mexican", "middle", "might", "military", "milk", "million", "mind", "mine", "minister", "minor",
            "minority", "minute", "miracle", "mirror", "miss", "missile", "mission", "mistake", "mix", "mixture",
            "mm-hmm",
            "mode", "model", "moderate", "modern", "modest", "mom", "moment", "money", "monitor", "month", "mood",
            "moon",
            "moral", "more", "moreover", "morning", "mortgage", "most", "mostly", "mother", "motion", "motivation",
            "motor", "mount", "mountain", "mouse", "mouth", "move", "movement", "movie", "Mr", "Mrs", "Ms", "much",
            "multiple", "murder", "muscle", "museum", "music", "musical", "musician", "Muslim", "must", "mutual", "my",
            "myself", "mystery", "myth", "naked", "name", "narrative", "narrow", "nation", "national", "native",
            "natural",
            "naturally", "nature", "near", "nearby", "nearly", "necessarily", "necessary", "neck", "need", "negative",
            "negotiate", "negotiation", "neighbor", "neighborhood", "neither", "nerve", "nervous", "net", "network",
            "never", "nevertheless", "new", "newly", "news", "newspaper", "next", "nice", "night", "nine", "no",
            "nobody",
            "nod", "noise", "nomination", "none", "nonetheless", "nor", "normal", "normally", "north", "northern",
            "nose",
            "not", "note", "nothing", "notice", "notion", "novel", "now", "nowhere", "not", "nuclear", "number",
            "numerous", "nurse", "nut", "object", "objective", "obligation", "observation", "observe", "observer",
            "obtain", "obvious", "obviously", "occasion", "occasionally", "occupation", "occupy", "occur", "ocean",
            "odd",
            "odds", "of", "off", "offense", "offensive", "offer", "office", "officer", "official", "often", "oh", "oil",
            "ok", "okay", "old", "Olympic", "on", "once", "one", "ongoing", "onion", "online", "only", "onto", "open",
            "opening", "operate", "operating", "operation", "operator", "opinion", "opponent", "opportunity", "oppose",
            "opposite", "opposition", "option", "or", "orange", "order", "ordinary", "organic", "organization",
            "organize",
            "orientation", "origin", "original", "originally", "other", "others", "otherwise", "ought", "our",
            "ourselves",
            "out", "outcome", "outside", "oven", "over", "overall", "overcome", "overlook", "owe", "own", "owner",
            "pace",
            "pack", "package", "page", "pain", "painful", "paint", "painter", "painting", "pair", "pale", "Palestinian",
            "palm", "pan", "panel", "pant", "paper", "parent", "park", "parking", "part", "participant", "participate",
            "participation", "particular", "particularly", "partly", "partner", "partnership", "party", "pass",
            "passage",
            "passenger", "passion", "past", "patch", "path", "patient", "pattern", "pause", "pay", "payment", "PC",
            "peace", "peak", "peer", "penalty", "people", "pepper", "per", "perceive", "percentage", "perception",
            "perfect", "perfectly", "perform", "performance", "perhaps", "period", "permanent", "permission", "permit",
            "person", "personal", "personality", "personally", "personnel", "perspective", "persuade", "pet", "phase",
            "phenomenon", "philosophy", "phone", "photo", "photograph", "photographer", "phrase", "physical",
            "physically",
            "physician", "piano", "pick", "picture", "pie", "piece", "pile", "pilot", "pine", "pink", "pipe", "pitch",
            "place", "plan", "plane", "planet", "planning", "plant", "plastic", "plate", "platform", "play", "player",
            "please", "pleasure", "plenty", "plot", "plus", "PM", "pocket", "poem", "poet", "poetry", "point", "pole",
            "police", "policy", "political", "politically", "politician", "politics", "poll", "pollution", "pool",
            "poor",
            "pop", "popular", "population", "porch", "port", "portion", "portrait", "portray", "pose", "position",
            "positive", "possess", "possibility", "possible", "possibly", "post", "pot", "potato", "potential",
            "potentially", "pound", "pour", "poverty", "powder", "power", "powerful", "practical", "practice", "pray",
            "prayer", "precisely", "predict", "prefer", "preference", "pregnancy", "pregnant", "preparation", "prepare",
            "prescription", "presence", "present", "presentation", "preserve", "president", "presidential", "press",
            "pressure", "pretend", "pretty", "prevent", "previous", "previously", "price", "pride", "priest",
            "primarily",
            "primary", "prime", "principal", "principle", "print", "prior", "priority", "prison", "prisoner", "privacy",
            "private", "probably", "problem", "procedure", "proceed", "process", "produce", "producer", "product",
            "production", "profession", "professional", "professor", "profile", "profit", "program", "progress",
            "project",
            "prominent", "promise", "promote", "prompt", "proof", "proper", "properly", "property", "proportion",
            "proposal", "propose", "proposed", "prosecutor", "prospect", "protect", "protection", "protein", "protest",
            "proud", "prove", "provide", "provider", "province", "provision", "psychological", "psychologist",
            "psychology", "public", "publication", "publicly", "publish", "publisher", "pull", "punishment", "purchase",
            "pure", "purpose", "pursue", "push", "put", "qualify", "quality", "quarter", "quarterback", "question",
            "quick", "quickly", "quiet", "quietly", "quit", "quite", "quote", "race", "racial", "radical", "radio",
            "rail",
            "rain", "raise", "range", "rank", "rapid", "rapidly", "rare", "rarely", "rate", "rather", "rating", "ratio",
            "raw", "reach", "react", "reaction", "read", "reader", "reading", "ready", "real", "reality", "realize",
            "really", "reason", "reasonable", "recall", "receive", "recent", "recently", "recipe", "recognition",
            "recognize", "recommend", "recommendation", "record", "recording", "recover", "recovery", "recruit", "red",
            "reduce", "reduction", "refer", "reference", "reflect", "reflection", "reform", "refugee", "refuse",
            "regard",
            "regarding", "regardless", "regime", "region", "regional", "register", "regular", "regularly", "regulate",
            "regulation", "reinforce", "reject", "relate", "relation", "relationship", "relative", "relatively",
            "relax",
            "release", "relevant", "relief", "religion", "religious", "rely", "remain", "remaining", "remarkable",
            "remember", "remind", "remote", "remove", "repeat", "repeatedly", "replace", "reply", "report", "reporter",
            "represent", "representation", "representative", "Republican", "reputation", "request", "require",
            "requirement", "research", "researcher", "resemble", "reservation", "resident", "resist", "resistance",
            "resolution", "resolve", "resort", "resource", "respect", "respond", "respondent", "response",
            "responsibility", "responsible", "rest", "restaurant", "restore", "restriction", "result", "retain",
            "retire",
            "retirement", "return", "reveal", "revenue", "review", "revolution", "rhythm", "rice", "rich", "rid",
            "ride",
            "rifle", "right", "ring", "rise", "risk", "river", "road", "rock", "role", "roll", "romantic", "roof",
            "room",
            "root", "rope", "rose", "rough", "roughly", "round", "route", "routine", "row", "rub", "rule", "run",
            "running", "rural", "rush", "Russian", "sacred", "sad", "safe", "safety", "sake", "salad", "salary", "sale",
            "sales", "salt", "same", "sample", "sanction", "sand", "satellite", "satisfaction", "satisfy", "sauce",
            "save",
            "saving", "say", "scale", "scandal", "scared", "scenario", "scene", "schedule", "scheme", "scholar",
            "scholarship", "school", "science", "scientific", "scientist", "scope", "score", "scream", "screen",
            "script",
            "sea", "search", "season", "seat", "second", "secret", "secretary", "section", "sector", "secure",
            "security",
            "see", "seed", "seek", "seem", "segment", "seize", "select", "selection", "self", "sell", "Senate",
            "senator",
            "send", "senior", "sense", "sensitive", "sentence", "separate", "sequence", "series", "serious",
            "seriously",
            "serve", "service", "session", "set", "setting", "settle", "settlement", "seven", "several", "severe",
            "sex",
            "sexual", "shade", "shadow", "shake", "shall", "shape", "share", "sharp", "she", "sheet", "shelf", "shell",
            "shelter", "shift", "shine", "ship", "shirt", "shit", "shock", "shoe", "shoot", "shooting", "shop",
            "shopping",
            "shore", "short", "shortly", "shot", "should", "shoulder", "shout", "show", "shower", "shrug", "shut",
            "sick",
            "side", "sigh", "sight", "sign", "signal", "significance", "significant", "significantly", "silence",
            "silent",
            "silver", "similar", "similarly", "simple", "simply", "sin", "since", "sing", "singer", "single", "sink",
            "sir", "sister", "sit", "site", "situation", "six", "size", "ski", "skill", "skin", "sky", "slave", "sleep",
            "slice", "slide", "slight", "slightly", "slip", "slow", "slowly", "small", "smart", "smell", "smile",
            "smoke",
            "smooth", "snap", "snow", "so", "so-called", "soccer", "social", "society", "soft", "software", "soil",
            "solar", "soldier", "solid", "solution", "solve", "some", "somebody", "somehow", "someone", "something",
            "sometimes", "somewhat", "somewhere", "son", "song", "soon", "sophisticated", "sorry", "sort", "soul",
            "sound",
            "soup", "source", "south", "southern", "Soviet", "space", "Spanish", "speak", "speaker", "special",
            "specialist", "species", "specific", "specifically", "speech", "speed", "spend", "spending", "spin",
            "spirit",
            "spiritual", "split", "spokesman", "sport", "spot", "spread", "spring", "square", "squeeze", "stability",
            "stable", "staff", "stage", "stair", "stake", "stand", "standard", "standing", "star", "stare", "start",
            "state", "statement", "station", "statistics", "status", "stay", "steady", "steal", "steel", "step",
            "stick",
            "still", "stir", "stock", "stomach", "stone", "stop", "storage", "store", "storm", "story", "straight",
            "strange", "stranger", "strategic", "strategy", "stream", "street", "strength", "strengthen", "stress",
            "stretch", "strike", "string", "strip", "stroke", "strong", "strongly", "structure", "struggle", "student",
            "studio", "study", "stuff", "stupid", "style", "subject", "submit", "subsequent", "substance",
            "substantial",
            "succeed", "success", "successful", "successfully", "such", "sudden", "suddenly", "sue", "suffer",
            "sufficient", "sugar", "suggest", "suggestion", "suicide", "suit", "summer", "summit", "sun", "super",
            "supply", "support", "supporter", "suppose", "supposed", "Supreme", "sure", "surely", "surface", "surgery",
            "surprise", "surprised", "surprising", "surprisingly", "surround", "survey", "survival", "survive",
            "survivor",
            "suspect", "sustain", "swear", "sweep", "sweet", "swim", "swing", "switch", "symbol", "symptom", "system",
            "table", "tablespoon", "tactic", "tail", "take", "tale", "talent", "talk", "tall", "tank", "tap", "tape",
            "target", "task", "taste", "tax", "taxpayer", "tea", "teach", "teacher", "teaching", "team", "tear",
            "teaspoon", "technical", "technique", "technology", "teen", "teenager", "telephone", "telescope",
            "television",
            "tell", "temperature", "temporary", "ten", "tend", "tendency", "tennis", "tension", "tent", "term", "terms",
            "terrible", "territory", "terror", "terrorism", "terrorist", "test", "testify", "testimony", "testing",
            "text",
            "than", "thank", "thanks", "that", "the", "theater", "their", "them", "theme", "themselves", "then",
            "theory",
            "therapy", "there", "therefore", "these", "they", "thick", "thin", "thing", "think", "thinking", "third",
            "thirty", "this", "those", "though", "thought", "thousand", "threat", "threaten", "three", "throat",
            "through",
            "throughout", "throw", "thus", "ticket", "tie", "tight", "time", "tiny", "tip", "tire", "tired", "tissue",
            "title", "to", "tobacco", "today", "toe", "together", "tomato", "tomorrow", "tone", "tongue", "tonight",
            "too",
            "tool", "tooth", "top", "topic", "toss", "total", "totally", "touch", "tough", "tour", "tourist",
            "tournament",
            "toward", "towards", "tower", "town", "toy", "trace", "track", "trade", "tradition", "traditional",
            "traffic",
            "tragedy", "trail", "train", "training", "transfer", "transform", "transformation", "transition",
            "translate",
            "transportation", "travel", "treat", "treatment", "treaty", "tree", "tremendous", "trend", "trial", "tribe",
            "trick", "trip", "troop", "trouble", "truck", "TRUE", "truly", "trust", "truth", "try", "tube", "tunnel",
            "turn", "TV", "twelve", "twenty", "twice", "twin", "two", "type", "typical", "typically", "ugly",
            "ultimate",
            "ultimately", "unable", "uncle", "under", "undergo", "understand", "understanding", "unfortunately",
            "uniform",
            "union", "unique", "unit", "United", "universal", "universe", "university", "unknown", "unless", "unlike",
            "unlikely", "until", "unusual", "up", "upon", "upper", "urban", "urge", "us", "use", "used", "useful",
            "user",
            "usual", "usually", "utility", "vacation", "valley", "valuable", "value", "variable", "variation",
            "variety",
            "various", "vary", "vast", "vegetable", "vehicle", "venture", "version", "versus", "very", "vessel",
            "veteran",
            "via", "victim", "victory", "video", "view", "viewer", "village", "violate", "violation", "violence",
            "violent", "virtually", "virtue", "virus", "visible", "vision", "visit", "visitor", "visual", "vital",
            "voice",
            "volume", "volunteer", "vote", "voter", "vs", "vulnerable", "wage", "wait", "wake", "walk", "wall",
            "wander",
            "want", "war", "warm", "warn", "warning", "wash", "waste", "watch", "water", "wave", "way", "we", "weak",
            "wealth", "wealthy", "weapon", "wear", "weather", "wedding", "week", "weekend", "weekly", "weigh", "weight",
            "welcome", "welfare", "well", "west", "western", "wet", "what", "whatever", "wheel", "when", "whenever",
            "where", "whereas", "whether", "which", "while", "whisper", "white", "who", "whole", "whom", "whose", "why",
            "wide", "widely", "widespread", "wife", "wild", "will", "willing", "win", "wind", "window", "wine", "wing",
            "winner", "winter", "wipe", "wire", "wisdom", "wise", "wish", "with", "withdraw", "within", "without",
            "witness", "woman", "wonder", "wonderful", "wood", "wooden", "word", "work", "worker", "working", "works",
            "workshop", "world", "worried", "worry", "worth", "would", "wound", "wrap", "write", "writer", "writing",
            "wrong", "yard", "yeah", "year", "yell", "yellow", "yes", "yesterday", "yet", "yield", "you", "young",
            "your",
            "yours", "yourself", "youth", "zone"]

# The Title of window
pygame.display.set_caption("TAcurracy")

# The Icon of the window
icon = pygame.image.load('data/keyboard.png')
pygame.display.set_icon(icon)
# dimensions of window
screenx = 1280
screeny = 720
# window: (width(x axis) , height(y axis))
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
# The background (images) of the Window:
backgroundT = pygame.image.load('data/BackgroundT.png')
background = pygame.image.load('data/background.png')
backgroundE = pygame.image.load('data/Background(esc).png')
backgroundEg = pygame.image.load('data/Background(esc)g.png')
wbackgroundEg = pygame.image.load('data/wBackground(esc)g.png')
backgroundEg2 = pygame.image.load('data/Background(esc)g2.png')
wbackgroundEg2 = pygame.image.load('data/wBackground(esc)g2.png')
loading = pygame.image.load('data/LoadingScreen.png')
results = pygame.image.load('data/Results.png')
results2 = pygame.image.load('data/Results2.png')
cwords = pygame.image.load('data/words.png')

# The background (audio(s)) of the game:
loaded = pygame.mixer.Sound('data/Loaded.mp3')
menunav = pygame.mixer.Sound('data/menuNav.mp3')
music = pygame.mixer.music.load('data/BackgroundMusic.mp3')
countdownsound = pygame.mixer.Sound('data/Countdownsound.mp3')

##########Title(Main Screen)##########
font130 = pygame.font.Font('data/FONT.TTF', 130)
maintitle = font130.render('TAccuracy', False, (255, 147, 0))
titlex = 20
titley = 130

font25 = pygame.font.Font('data/FONT.TTF', 25)
x = 'Press Enter to Start'
submaintitle = font25.render(x, False, (255, 255, 255))
stitlex = 30
stitley = 400

namemaintitle = font25.render('Atassi Productions', False, (255, 255, 255))
ntitlex = 850
ntitley = 670
######################################

##########Main(Main Menu)###########
MAX = 217.5

font50 = pygame.font.Font('data/FONT.TTF', 50)
ffont50 = pygame.font.Font('data/FONT2.ttf', 50)
start = font50.render('StartGame', False, (255, 255, 255))
startx = (screenx / 2) - 230
starty = (screeny / 2) - 100
START = 267.5

setting = font50.render('Settings', False, (255, 255, 255))
settingx = (screenx / 2) - 180
settingy = (screeny / 2) - 50
SETTING = 317.5

credit = font50.render('Credits', False, (255, 255, 255))
creditx = (screenx / 2) - 155
credity = (screeny / 2) + 0
CREDIT = 367.5

exit = font50.render('Exit', False, (255, 255, 255))
exitx = (screenx / 2) - 80
exity = (screeny / 2) + 50
EXIT = 417.5

MIN = 467.5
######################################
##########GAME(GAME Menu)###########
GMAX = 247.5

font75 = pygame.font.Font('data/FONT.TTF', 75)
ffont75 = pygame.font.Font('data/FONT2.ttf', 75)
option = font75.render('Choose An Option', False, (255, 255, 255))
optionx = 102.5
optiony = 160
OPTION = 267.5

timed = font75.render('Timed', False, (255, 255, 255))
timedx = 460
timedy = 320
TIMED = 367.5

words = font75.render('Words', False, (255, 255, 255))
wordsx = 440
wordsy = 410
WORDS = 417.5

GMIN = 517.5
######################################
##########TIMED(GAME Menu)###########
OMAX = 175

time = font75.render('Choose A Time', False, (255, 255, 255))
timex = 194.5
timey = 110
TIME = 267.5

sixty = font75.render('60', False, (255, 255, 255))
sixtyx = 571
sixtyy = 250
SIXTY = 367.5

onetwenty = font75.render('120', False, (255, 255, 255))
onetwentyx = 547.5
onetwentyy = 400
ONETWENTY = 417.5

oneeighty = font75.render('180', False, (255, 255, 255))
oneeightyx = 547.5
oneeightyy = 550
ONEEIGHTY = 417.5

OMIN = 625
######################################
music = font50.render('Music', False, (255, 255, 255))
musicx = 515
musicy = 110
# 200px y between
sound = font50.render('Sound', False, (255, 255, 255))
soundx = 515
soundy = 310

nw = font50.render('Next Word', False, (255, 255, 255))
nwx = 419.5
nwy = 510

SMAX = 115
Y1 = font50.render('Y', False, (255, 255, 255))
Y1x = 615
Y1y = 160
Y1c = 165

N1 = font50.render('N', False, (255, 255, 255))
N1x = 615
N1y = 210
N1c = 215

Y2 = font50.render('Y', False, (255, 255, 255))
Y2x = 615
Y2y = 360
Y2c = 365

N2 = font50.render('N', False, (255, 255, 255))
N2x = 615
N2y = 410
N2c = 415

Y3 = font50.render('Enter', False, (255, 255, 255))
Y3x = 515
Y3y = 560
Y3c = 565

N3 = font50.render('Space', False, (255, 255, 255))
N3x = 515
N3y = 610
N3c = 615
SMIN = 665
######################################
font400 = pygame.font.Font('data/FONT.TTF', 400)
three = font400.render('3', False, (255, 255, 255))
countx = 506
onex = 556
county = 150
two = font400.render('2', False, (255, 255, 255))
one = font400.render('1', False, (255, 255, 255))
######################################
font100 = pygame.font.Font('data/FONT.TTF', 100)
ffont100 = pygame.font.Font('data/FONT2.ttf', 100)
accx = 714
accy = 437
font19 = pygame.font.Font('data/FONT.TTF', 19)
endingx = 48
endingy = 690
wpmx = 774
wpmy = 290
######################################
def resultpage(wpm, accuracy, ending):
    screen.blit(results, [0, 0])
    screen.blit((font100.render(accuracy, False, (255, 255, 255))), (accx, accy))
    screen.blit((font19.render(ending, False, (255, 255, 255))), (endingx, endingy))
    screen.blit((font100.render(wpm, False, (255, 255, 255))), (accx, wpmy))

def resultpage1(accuracy, ending):
    screen.blit(results2, [0, 0])
    screen.blit((font100.render(accuracy, False, (255, 255, 255))), (accx, accy))
    screen.blit((font19.render(ending, False, (255, 255, 255))), (endingx, endingy))

def outputting(z, z2):
    if enterbutton == 1:
        screen.blit(backgroundEg, [0, 0])
    if spacebutton == 1:
        screen.blit(backgroundEg2, [0, 0])
    screen.blit(ffont100.render(thewords[z], False, (255, 255, 255)), (176, 220))
    screen.blit(ffont50.render(thewords[z2], False, (255, 255, 255)), (176, 160))
    pygame.display.update()

def woutputting(z, z2):
    if enterbutton == 1:
        screen.blit(wbackgroundEg, [0, 0])
    if spacebutton == 1:
        screen.blit(wbackgroundEg2, [0, 0])
    screen.blit(ffont100.render(thewords[z], False, (255, 255, 255)), (176, 220))
    screen.blit(ffont50.render(thewords[z2], False, (255, 255, 255)), (176, 160))
    pygame.display.update()


def typing(text2):
    screen.blit(ffont50.render(text2, False, (255, 255, 255)), (119, 413))

def choosing():
    screen.blit(cwords, [0, 0])

def timer():
    if vol == True:
        pygame.mixer.Sound.play(countdownsound)
    screen.blit(background, [0, 0])
    screen.blit(three, (countx, county))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.blit(background, [0, 0])
    screen.blit(two, (countx, county))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.blit(background, [0, 0])
    screen.blit(one, (onex, county))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.blit(background, [0, 0])
    pygame.display.update()
    pygame.time.wait(1000)


def gmenu():
    screen.blit(backgroundE, [0, 0])
    screen.blit(option, (optionx, optiony))
    screen.blit(timed, (timedx, timedy))
    screen.blit(words, (wordsx, wordsy))


def tmenu():
    screen.blit(backgroundE, [0, 0])
    screen.blit(time, (timex, timey))
    screen.blit(sixty, (sixtyx, sixtyy))
    screen.blit(onetwenty, (onetwentyx, onetwentyy))
    screen.blit(oneeighty, (oneeightyx, oneeightyy))


def settings():
    screen.blit(backgroundE, [0, 0])
    screen.blit(music, (musicx, musicy))
    screen.blit(Y1, (Y1x, Y1y))
    screen.blit(N1, (N1x, N1y))
    screen.blit(sound, (soundx, soundy))
    screen.blit(Y2, (Y2x, Y2y))
    screen.blit(N2, (N2x, N2y))
    screen.blit(nw, (nwx, nwy))
    screen.blit(Y3, (Y3x, Y3y))
    screen.blit(N3, (N3x, N3y))


def fadein():
    fadein = pygame.Surface((1280, 720))
    fadein.fill((0, 0, 0))
    for alpha in range(0, 300):
        fadein.set_alpha(alpha)
        screen.blit(fadein, (0, 0))
        pygame.display.update()
        pygame.time.delay(2)


def title(x):
    screen.blit(backgroundT, [0, 0])
    screen.blit(maintitle, (titlex, titley))
    screen.blit(namemaintitle, (ntitlex, ntitley))
    screen.blit(font50.render(x, False, (255, 255, 255)), (stitlex, stitley))


def loadingS():
    screen.blit(loading, [0, 0])
    pygame.display.update()
    clock.tick(60)


def mainmenu():
    screen.blit(background, [0, 0])
    screen.blit(start, (startx, starty))
    screen.blit(exit, (exitx, exity))
    screen.blit(setting, (settingx, settingy))
    screen.blit(credit, (creditx, credity))


def cursor1(h1, w1, cursor1y):
    cursor1x = (screenx / 2) - 290
    pygame.draw.rect(screen, (255, 255, 255), [cursor1x, cursor1y, w1, h1])
    cursor2x = (screenx / 2) + 255  # 25
    pygame.draw.rect(screen, (255, 255, 255), [cursor2x, cursor1y, w1, h1])


def cursor2(h1, w1, cursor1y2):
    cursor1x = (screenx / 2) - 290
    pygame.draw.rect(screen, (255, 255, 255), [cursor1x, cursor1y2, w1, h1])
    cursor2x = (screenx / 2) + 255  # 25
    pygame.draw.rect(screen, (255, 255, 255), [cursor2x, cursor1y2, w1, h1])


def cursor3(h1, w1, cursor1y3):
    cursor1x = (screenx / 2) - 290
    pygame.draw.rect(screen, (255, 255, 255), [cursor1x, cursor1y3, w1, h1])
    cursor2x = (screenx / 2) + 255  # 25
    pygame.draw.rect(screen, (255, 255, 255), [cursor2x, cursor1y3, w1, h1])


def cursor4(h1, w1, cursor1y4):
    cursor1x = (screenx / 2) - 290
    pygame.draw.rect(screen, (255, 255, 255), [cursor1x, cursor1y4, w1, h1])
    cursor2x = (screenx / 2) + 255  # 25
    pygame.draw.rect(screen, (255, 255, 255), [cursor2x, cursor1y4, w1, h1])


crashed = False
enter = False
while not enter:
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        fadein()
        loadingS()
        pygame.display.update()
        pygame.time.wait(5000)
        crashed = True
        fadein()
        pygame.mixer.music.play(-1)
    x = 'Press Enter to Start'
    title(x)
    pygame.display.update()
    pygame.time.wait(500)  # 500 = 0.5 seconds
    x = ''
    title(x)
    pygame.display.update()
    pygame.time.wait(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.mixer.Sound.play(loaded)
                enter = True

fadein()
h1 = 40
w1 = 40
vol = True
change = 0
cursor1y = START
cursor1y2 = 1
enter1 = False
while not enter1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                if cursor1y2 == Y1c:
                    pygame.mixer.music.unpause()
                if cursor1y2 == N1c:
                    pygame.mixer.music.pause()
                if cursor1y2 == Y2c:
                    pygame.mixer.unpause()
                    vol = True
                if cursor1y2 == N2c:
                    pygame.mixer.stop()
                    vol = False
            if event.key == pygame.K_ESCAPE:
                enter3 = True
                enter2 = True
            if event.key == pygame.K_DOWN:
                if cursor1y2 == N1c or cursor1y2 == N2c:
                    change = 150
                    cursor1y2 += change
                    cursor2(h1, w1, cursor1y2)
                    pygame.display.update()
                    if vol == True:
                        pygame.mixer.Sound.play(menunav)
                else:
                    change = 50
                    cursor1y2 += change
                    if cursor1y2 == SMIN:
                        cursor1y2 = 165
                        if vol == True:
                            pygame.mixer.Sound.play(menunav)
                    cursor2(h1, w1, cursor1y2)
                    pygame.display.update()
                    if vol == True:
                        pygame.mixer.Sound.play(menunav)
            if event.key == pygame.K_UP:
                if cursor1y2 == Y2c or cursor1y2 == Y3c:
                    change = -150
                    cursor1y2 += change
                    cursor2(h1, w1, cursor1y2)
                    pygame.display.update()
                    if vol == True:
                        pygame.mixer.Sound.play(menunav)
                else:
                    change = -50
                    cursor1y2 += change
                    if cursor1y2 == SMAX:
                        cursor1y2 = 615
                        if vol == True:
                            pygame.mixer.Sound.play(menunav)
                    if vol == True:
                        pygame.mixer.Sound.play(menunav)
                    cursor2(h1, w1, cursor1y2)
                    pygame.display.update()
    mainmenu()
    h1 = 40
    w1 = 40
    cursor1(h1, w1, cursor1y)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                change = 50
                cursor1y += change
                if vol == True:
                    pygame.mixer.Sound.play(menunav)
                if cursor1y == MIN:
                    cursor1y = (screeny / 2) - 92.5
                cursor1(h1, w1, cursor1y)
                pygame.display.update()
            if event.key == pygame.K_UP:
                change = -50
                cursor1y += change
                if vol == True:
                    pygame.mixer.Sound.play(menunav)
                if cursor1y == MAX:
                    cursor1y = ((screeny / 2) - 92.5) + 150
                cursor1(h1, w1, cursor1y)
                pygame.display.update()
            if event.key == pygame.K_RETURN:

                enter2 = False
                while not enter2:
                    if cursor1y == CREDIT:
                        screen.blit(pygame.image.load('data/Credit.png'), [0, 0])
                        pygame.display.update()
                        event = pygame.event.wait()
                        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                            enter2 = True
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                    if cursor1y == SETTING:
                        h1 = 40
                        w1 = 40
                        cursor1y2 = 165
                        settings()
                        cursor2(h1, w1, cursor1y2)
                        pygame.display.update()

                        enter3 = False
                        while not enter3:
                            settings()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RETURN:
                                        if cursor1y2 == Y1c:
                                            pygame.mixer.music.unpause()
                                        if cursor1y2 == N1c:
                                            pygame.mixer.music.pause()
                                        if cursor1y2 == Y2c:
                                            pygame.mixer.unpause()
                                            vol = True
                                        if cursor1y2 == N2c:
                                            pygame.mixer.stop()
                                            vol = False
                                        if cursor1y2 == Y3c:
                                            enterbutton = 1
                                            spacebutton = 0
                                        if cursor1y2 == N3c:
                                            enterbutton = 0
                                            spacebutton = 1

                                    if event.key == pygame.K_ESCAPE:
                                        enter3 = True
                                        enter2 = True
                                    if event.key == pygame.K_DOWN:
                                        if cursor1y2 == N1c or cursor1y2 == N2c:
                                            change = 150
                                            cursor1y2 += change
                                            cursor2(h1, w1, cursor1y2)
                                            pygame.display.update()
                                            if vol == True:
                                                pygame.mixer.Sound.play(menunav)
                                        else:
                                            change = 50
                                            cursor1y2 += change
                                            if cursor1y2 == SMIN:
                                                cursor1y2 = 165
                                                if vol == True:
                                                    pygame.mixer.Sound.play(menunav)
                                            cursor2(h1, w1, cursor1y2)
                                            pygame.display.update()
                                            if vol == True:
                                                pygame.mixer.Sound.play(menunav)
                                    if event.key == pygame.K_UP:
                                        if cursor1y2 == Y2c or cursor1y2 == Y3c:
                                            change = -150
                                            cursor1y2 += change
                                            cursor2(h1, w1, cursor1y2)
                                            pygame.display.update()
                                            if vol == True:
                                                pygame.mixer.Sound.play(menunav)
                                        else:
                                            change = -50
                                            cursor1y2 += change
                                            if cursor1y2 == SMAX:
                                                cursor1y2 = 615
                                                if vol == True:
                                                    pygame.mixer.Sound.play(menunav)
                                            if vol == True:
                                                pygame.mixer.Sound.play(menunav)
                                            cursor2(h1, w1, cursor1y2)
                                            pygame.display.update()
                    if cursor1y == EXIT:
                        fadein()
                        screen.blit(pygame.image.load('data/EndingScreen.png'), [0, 0])
                        pygame.display.update()
                        pygame.time.wait(2000)
                        pygame.quit()
                        sys.exit()

                    if cursor1y == START:
                        h1 = 50
                        w1 = 50
                        cursor1y3 = 337.5
                        gmenu()
                        cursor3(h1, w1, cursor1y3)
                        pygame.display.update()
                        enter4 = False
                        if cursor1y3 == 337.5:
                            while not enter4:
                                gmenu()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            enter4 = True
                                            enter3 = True
                                            enter2 = True
                                        if event.key == pygame.K_DOWN:
                                            change = 90
                                            cursor1y3 += change
                                            if cursor1y3 == GMIN:
                                                cursor1y3 = 337.5
                                                if vol == True:
                                                    pygame.mixer.Sound.play(menunav)
                                            if vol == True:
                                                pygame.mixer.Sound.play(menunav)
                                            cursor3(h1, w1, cursor1y3)
                                            pygame.display.update()

                                        if event.key == pygame.K_UP:
                                            change = -90
                                            cursor1y3 += change
                                            if cursor1y3 == GMAX:
                                                cursor1y3 = 427.5
                                                if vol == True:
                                                    pygame.mixer.Sound.play(menunav)
                                            if vol == True:
                                                pygame.mixer.Sound.play(menunav)
                                            cursor3(h1, w1, cursor1y3)
                                            pygame.display.update()

                                        if event.key == pygame.K_RETURN:
                                            if cursor1y3 == 337.5:
                                                tester = 0
                                                h1 = 50
                                                w1 = 50
                                                cursor1y4 = 268
                                                enter45 = False
                                                while not enter45:
                                                 tmenu()
                                                 cursor4(h1, w1, cursor1y4)
                                                 pygame.display.update()
                                                 enter45 = True

                                                enter5 = False
                                                while not enter5:
                                                    tmenu()
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.quit()
                                                            sys.exit()
                                                        if event.type == pygame.KEYDOWN:
                                                            if event.key == pygame.K_DOWN:
                                                                change = 150
                                                                cursor1y4 += change
                                                                if cursor1y4 == 718:
                                                                    cursor1y4 = 268
                                                                    if vol == True:
                                                                        pygame.mixer.Sound.play(menunav)
                                                                if vol == True:
                                                                    pygame.mixer.Sound.play(menunav)
                                                                cursor4(h1, w1, cursor1y4)
                                                                pygame.display.update()

                                                            if event.key == pygame.K_UP:
                                                                change = -150
                                                                cursor1y4 += change
                                                                if cursor1y4 == 118:
                                                                    cursor1y4 = 568
                                                                    if vol == True:
                                                                        pygame.mixer.Sound.play(menunav)
                                                                if vol == True:
                                                                    pygame.mixer.Sound.play(menunav)
                                                                cursor4(h1, w1, cursor1y4)
                                                                pygame.display.update()

                                                            if event.key == pygame.K_ESCAPE:
                                                                enter5 = True
                                                                enter4 = True
                                                                enter3 = True
                                                            if event.key == pygame.K_RETURN:
                                                                text2 = ''
                                                                counter = 0
                                                                tdifference = 0
                                                                currenttime = pygame.time.get_ticks()
                                                                gametimer = pygame.time.get_ticks() - currenttime
                                                                if cursor1y4 == 268:
                                                                    seconds = 64000
                                                                    timepress = 10000 + currenttime
                                                                    timer()
                                                                    z = random.randint(0, 2999)
                                                                    z2 = random.randint(0, 2999)
                                                                    pygame.display.update()
                                                                    outputting(z, z2)
                                                                    while pygame.time.get_ticks() - currenttime < seconds:
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.type == pygame.KEYDOWN:
                                                                                if event.type == pygame.QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_ESCAPE:
                                                                                    seconds = 0
                                                                                    enter45 = False
                                                                                    enter5 = True
                                                                                    enter4 = True
                                                                                    enter6 = True
                                                                                    tester = 1
                                                                                if event.key == pygame.K_BACKSPACE:
                                                                                    text2 = text2[:-1]
                                                                                    outputting(z, z2)
                                                                                    typing(text2)
                                                                                    pygame.display.update()
                                                                                if enterbutton == 1:
                                                                                    if event.key == pygame.K_RETURN:
                                                                                        char = len(text2)
                                                                                        tchar += char
                                                                                        counter += 1
                                                                                        seq = difflib.SequenceMatcher(
                                                                                            isjunk=None, a=thewords[z], b=text2)
                                                                                        difference = seq.quick_ratio() * 100
                                                                                        total = int(difference)
                                                                                        tdifference += total
                                                                                        text2 = ''
                                                                                        z = z2
                                                                                        z2 = random.randint(0, 2999)
                                                                                        outputting(z, z2)
                                                                                        pygame.display.update()
                                                                                        wpm = (tchar/5)/1
                                                                                        accuracy = int(accuracy)
                                                                                        accuracy = tdifference / counter
                                                                                        accuracy = round(accuracy)
                                                                                        wpm = round(wpm)
                                                                                    else:
                                                                                        text2 += event.unicode
                                                                                        typing(text2)
                                                                                        pygame.display.update()
                                                                                if spacebutton == 1:
                                                                                    if event.key == pygame.K_SPACE:
                                                                                        char = len(text2)
                                                                                        tchar += char
                                                                                        counter += 1
                                                                                        seq = difflib.SequenceMatcher(
                                                                                            isjunk=None, a=thewords[z],
                                                                                            b=text2)
                                                                                        difference = seq.quick_ratio() * 100
                                                                                        total = int(difference)
                                                                                        tdifference += total
                                                                                        text2 = ''
                                                                                        z = z2
                                                                                        z2 = random.randint(0, 2999)
                                                                                        outputting(z, z2)
                                                                                        pygame.display.update()
                                                                                        wpm = (tchar / 5) / 1
                                                                                        accuracy = int(accuracy)
                                                                                        accuracy = tdifference / counter
                                                                                        accuracy = round(accuracy)
                                                                                        wpm = round(wpm)
                                                                                    else:
                                                                                        text2 += event.unicode
                                                                                        typing(text2)
                                                                                        pygame.display.update()
                                                                    accuracy = str(accuracy)
                                                                    wpm = str(wpm)
                                                                    if tester == 0:
                                                                        enter6 = False
                                                                    while not enter6:
                                                                        ending = 'press enter to return to the main menu           press space to exit game'
                                                                        resultpage(wpm, accuracy, ending)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(500)
                                                                        ending = ''
                                                                        resultpage(wpm, accuracy, ending)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(500)
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.type == pygame.KEYDOWN:
                                                                                if event.key == pygame.K_SPACE:
                                                                                    fadein()
                                                                                    screen.blit(
                                                                                        pygame.image.load('data/EndingScreen.png'),
                                                                                        [0, 0])
                                                                                    pygame.display.update()
                                                                                    pygame.time.wait(2000)
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_RETURN:
                                                                                    enter6 = True
                                                                                    enter45 = False
                                                                                    enter5 = True
                                                                                    enter4 = True
                                                                if cursor1y4 == 418:
                                                                    seconds = 124000
                                                                    timepress = 10000 + currenttime
                                                                    timer()
                                                                    z = random.randint(0, 2999)
                                                                    z2 = random.randint(0, 2999)
                                                                    pygame.display.update()
                                                                    outputting(z, z2)
                                                                    while pygame.time.get_ticks() - currenttime < seconds:
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.type == pygame.KEYDOWN:
                                                                                if event.type == pygame.QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_ESCAPE:
                                                                                    seconds = 0
                                                                                    enter45 = False
                                                                                    enter5 = True
                                                                                    enter4 = True
                                                                                    enter6 = True
                                                                                    tester = 1
                                                                                if event.key == pygame.K_BACKSPACE:
                                                                                    text2 = text2[:-1]
                                                                                    outputting(z, z2)
                                                                                    typing(text2)
                                                                                    pygame.display.update()
                                                                                if enterbutton == 1:
                                                                                    if event.key == pygame.K_RETURN:
                                                                                        char = len(text2)
                                                                                        tchar += char
                                                                                        counter += 1
                                                                                        seq = difflib.SequenceMatcher(
                                                                                            isjunk=None, a=thewords[z],
                                                                                            b=text2)
                                                                                        difference = seq.quick_ratio() * 100
                                                                                        total = int(difference)
                                                                                        tdifference += total
                                                                                        text2 = ''
                                                                                        z = z2
                                                                                        z2 = random.randint(0, 2999)
                                                                                        outputting(z, z2)
                                                                                        pygame.display.update()
                                                                                        wpm = (tchar / 5) / 2
                                                                                        accuracy = int(accuracy)
                                                                                        accuracy = tdifference / counter
                                                                                        accuracy = round(accuracy)
                                                                                        wpm = round(wpm)
                                                                                    else:
                                                                                        text2 += event.unicode
                                                                                        typing(text2)
                                                                                        pygame.display.update()
                                                                                if spacebutton == 1:
                                                                                    if event.key == pygame.K_SPACE:
                                                                                        char = len(text2)
                                                                                        tchar += char
                                                                                        counter += 1
                                                                                        seq = difflib.SequenceMatcher(
                                                                                            isjunk=None, a=thewords[z],
                                                                                            b=text2)
                                                                                        difference = seq.quick_ratio() * 100
                                                                                        total = int(difference)
                                                                                        tdifference += total
                                                                                        text2 = ''
                                                                                        z = z2
                                                                                        z2 = random.randint(0, 2999)
                                                                                        outputting(z, z2)
                                                                                        pygame.display.update()
                                                                                        wpm = (tchar / 5) / 2
                                                                                        accuracy = int(accuracy)
                                                                                        accuracy = tdifference / counter
                                                                                        accuracy = round(accuracy)
                                                                                        wpm = round(wpm)
                                                                                    else:
                                                                                        text2 += event.unicode
                                                                                        typing(text2)
                                                                                        pygame.display.update()
                                                                    accuracy = str(accuracy)
                                                                    wpm = str(wpm)
                                                                    if tester == 0:
                                                                        enter6 = False
                                                                    while not enter6:
                                                                        ending = 'press enter to return to the main menu           press space to exit game'
                                                                        resultpage(wpm, accuracy, ending)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(500)
                                                                        ending = ''
                                                                        resultpage(wpm, accuracy, ending)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(500)
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.type == pygame.KEYDOWN:
                                                                                if event.key == pygame.K_SPACE:
                                                                                    fadein()
                                                                                    screen.blit(
                                                                                        pygame.image.load(
                                                                                            'data/EndingScreen.png'),
                                                                                        [0, 0])
                                                                                    pygame.display.update()
                                                                                    pygame.time.wait(2000)
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_RETURN:
                                                                                    enter6 = True
                                                                                    enter45 = False
                                                                                    enter5 = True
                                                                                    enter4 = True
                                                                if cursor1y4 == 568:
                                                                    seconds = 184000
                                                                    timepress = 10000 + currenttime
                                                                    timer()
                                                                    z = random.randint(0, 2999)
                                                                    z2 = random.randint(0, 2999)
                                                                    pygame.display.update()
                                                                    outputting(z, z2)
                                                                    while pygame.time.get_ticks() - currenttime < seconds:
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.type == pygame.KEYDOWN:
                                                                                if event.type == pygame.QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_ESCAPE:
                                                                                    seconds = 0
                                                                                    enter45 = False
                                                                                    enter5 = True
                                                                                    enter4 = True
                                                                                    enter6 = True
                                                                                    tester = 1
                                                                                if event.key == pygame.K_BACKSPACE:
                                                                                    text2 = text2[:-1]
                                                                                    outputting(z, z2)
                                                                                    typing(text2)
                                                                                    pygame.display.update()
                                                                                if enterbutton == 1:
                                                                                    if event.key == pygame.K_RETURN:
                                                                                        char = len(text2)
                                                                                        tchar += char
                                                                                        counter += 1
                                                                                        seq = difflib.SequenceMatcher(
                                                                                            isjunk=None, a=thewords[z],
                                                                                            b=text2)
                                                                                        difference = seq.quick_ratio() * 100
                                                                                        total = int(difference)
                                                                                        tdifference += total
                                                                                        text2 = ''
                                                                                        z = z2
                                                                                        z2 = random.randint(0, 2999)
                                                                                        outputting(z, z2)
                                                                                        pygame.display.update()
                                                                                        wpm = (tchar / 5) / 3
                                                                                        accuracy = int(accuracy)
                                                                                        accuracy = tdifference / counter
                                                                                        accuracy = round(accuracy)
                                                                                        wpm = round(wpm)
                                                                                    else:
                                                                                        text2 += event.unicode
                                                                                        typing(text2)
                                                                                        pygame.display.update()
                                                                                if spacebutton == 1:
                                                                                    if event.key == pygame.K_SPACE:
                                                                                        char = len(text2)
                                                                                        tchar += char
                                                                                        counter += 1
                                                                                        seq = difflib.SequenceMatcher(
                                                                                            isjunk=None, a=thewords[z],
                                                                                            b=text2)
                                                                                        difference = seq.quick_ratio() * 100
                                                                                        total = int(difference)
                                                                                        tdifference += total
                                                                                        text2 = ''
                                                                                        z = z2
                                                                                        z2 = random.randint(0, 2999)
                                                                                        outputting(z, z2)
                                                                                        pygame.display.update()
                                                                                        wpm = (tchar / 5) / 3
                                                                                        accuracy = int(accuracy)
                                                                                        accuracy = tdifference / counter
                                                                                        accuracy = round(accuracy)
                                                                                        wpm = round(wpm)
                                                                                    else:
                                                                                        text2 += event.unicode
                                                                                        typing(text2)
                                                                                        pygame.display.update()
                                                                    accuracy = str(accuracy)
                                                                    wpm = str(wpm)
                                                                    if tester == 0:
                                                                        enter6 = False
                                                                    while not enter6:
                                                                        ending = 'press enter to return to the main menu           press space to exit game'
                                                                        resultpage(wpm, accuracy, ending)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(500)
                                                                        ending = ''
                                                                        resultpage(wpm, accuracy, ending)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(500)
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.type == pygame.KEYDOWN:
                                                                                if event.type == pygame.QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_SPACE:
                                                                                    fadein()
                                                                                    screen.blit(
                                                                                        pygame.image.load(
                                                                                            'data/EndingScreen.png'),
                                                                                        [0, 0])
                                                                                    pygame.display.update()
                                                                                    pygame.time.wait(2000)
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                if event.key == pygame.K_RETURN:
                                                                                    enter6 = True
                                                                                    enter45 = False
                                                                                    enter5 = True
                                                                                    enter4 = True
                                            if cursor1y3 == 427.5:
                                                enter7 = False
                                                text2 = ''
                                                counter1 = ''
                                                choosing()
                                                typing(counter1)
                                                pygame.display.update()
                                                counter = 0
                                                while not enter7:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.quit()
                                                            sys.exit()
                                                        if event.type == pygame.KEYDOWN:
                                                            if event.key == pygame.K_ESCAPE:
                                                                enter7 = True
                                                                enter6 = True
                                                                enter45 = False
                                                                enter5 = True
                                                                enter4 = True
                                                            if event.key == pygame.K_BACKSPACE:
                                                                counter1 = counter1[:-1]
                                                                choosing()
                                                                typing(counter1)
                                                                pygame.display.update()
                                                            if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                                                                counter1 += event.unicode
                                                                choosing()
                                                                typing(counter1)
                                                                pygame.display.update()
                                                            if event.key == pygame.K_RETURN:
                                                                counter1 = int(counter1)
                                                                timer()
                                                                z = random.randint(0, 2999)
                                                                z2 = random.randint(0, 2999)
                                                                pygame.display.update()
                                                                woutputting(z, z2)
                                                                counter = 0
                                                                tdifference = 0
                                                                enter100 = True
                                                                while (counter1 > counter):
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()
                                                                        if event.type == pygame.KEYDOWN:
                                                                            if event.key == pygame.K_ESCAPE:
                                                                                enter7 = True
                                                                                enter6 = True
                                                                                enter45 = False
                                                                                enter5 = True
                                                                                enter4 = True
                                                                                counter = 999999999999999999999999999999
                                                                            if event.key == pygame.K_BACKSPACE:
                                                                                text2 = text2[:-1]
                                                                                woutputting(z, z2)
                                                                                typing(text2)
                                                                                pygame.display.update()
                                                                            if enterbutton == 1:
                                                                                if event.key == pygame.K_RETURN:
                                                                                    char = len(text2)
                                                                                    tchar += char
                                                                                    counter += 1
                                                                                    seq = difflib.SequenceMatcher(
                                                                                        isjunk=None, a=thewords[z],
                                                                                        b=text2)
                                                                                    difference = seq.quick_ratio() * 100
                                                                                    total = int(difference)
                                                                                    tdifference += total
                                                                                    text2 = ''
                                                                                    z = z2
                                                                                    z2 = random.randint(0, 2999)
                                                                                    woutputting(z, z2)
                                                                                    pygame.display.update()
                                                                                    accuracy = int(accuracy)
                                                                                    accuracy = tdifference / counter
                                                                                    accuracy = round(accuracy)
                                                                                else:
                                                                                    text2 += event.unicode
                                                                                    typing(text2)
                                                                                    pygame.display.update()
                                                                            if spacebutton == 1:
                                                                                if event.key == pygame.K_SPACE:
                                                                                    char = len(text2)
                                                                                    tchar += char
                                                                                    counter += 1
                                                                                    seq = difflib.SequenceMatcher(
                                                                                        isjunk=None, a=thewords[z],
                                                                                        b=text2)
                                                                                    difference = seq.quick_ratio() * 100
                                                                                    total = int(difference)
                                                                                    tdifference += total
                                                                                    text2 = ''
                                                                                    z = z2
                                                                                    z2 = random.randint(0, 2999)
                                                                                    woutputting(z, z2)
                                                                                    pygame.display.update()
                                                                                    accuracy = int(accuracy)
                                                                                    accuracy = tdifference / counter
                                                                                    accuracy = round(accuracy)
                                                                                else:
                                                                                    text2 += event.unicode
                                                                                    typing(text2)
                                                                                    pygame.display.update()
                                                                accuracy = str(accuracy)
                                                                if tester == 0:
                                                                    enter6 = False
                                                                while not enter6:
                                                                    ending = 'press enter to return to the main menu           press space to exit game'
                                                                    resultpage1(accuracy, ending)
                                                                    pygame.display.update()
                                                                    pygame.time.wait(500)
                                                                    ending = ''
                                                                    resultpage1(accuracy, ending)
                                                                    pygame.display.update()
                                                                    pygame.time.wait(500)
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()
                                                                        if event.type == pygame.KEYDOWN:
                                                                            if event.type == pygame.QUIT:
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.key == pygame.K_SPACE:
                                                                                fadein()
                                                                                screen.blit(
                                                                                    pygame.image.load(
                                                                                        'data/EndingScreen.png'),
                                                                                    [0, 0])
                                                                                pygame.display.update()
                                                                                pygame.time.wait(2000)
                                                                                pygame.quit()
                                                                                sys.exit()
                                                                            if event.key == pygame.K_RETURN:
                                                                                enter7 = True
                                                                                enter6 = True
                                                                                enter45 = False
                                                                                enter5 = True
                                                                                enter4 = True