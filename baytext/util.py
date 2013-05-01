#-*- encoding: utf-8 -*-

english_ignore = set("""
a able about above abroad according accordingly across actually adj after
afterwards again against ago ahead ain't all allow allows almost alone along
alongside already also although always am amid amidst among amongst an and
another any anybody anyhow anyone anything anyway anyways anywhere apart
appear appreciate appropriate are aren't around as a's aside ask asking
associated at available away awfully b back backward backwards be became
because become becomes becoming been before beforehand begin behind being
believe below beside besides best better between beyond both brief but by c
came can cannot cant can't caption cause causes certain certainly changes
clearly c'mon co co. com come comes concerning consequently consider
considering contain containing contains corresponding could couldn't course
c's currently d dare daren't definitely described despite did didn't different
directly do does doesn't doing done don't down downwards during e each edu eg
eight eighty either else elsewhere end ending enough entirely especially et
etc even ever evermore every everybody everyone everything everywhere ex
exactly example except f fairly far farther few fewer fifth first five
followed following follows for forever former formerly forth forward found
four from further furthermore g get gets getting given gives go goes going
gone got gotten greetings h had hadn't half happens hardly has hasn't have
haven't having he he'd he'll hello help hence her here hereafter hereby herein
here's hereupon hers herself he's hi him himself his hither hopefully how
howbeit however hundred i i'd ie if ignored i'll i'm immediate in inasmuch inc
inc. indeed indicate indicated indicates inner inside insofar instead into
inward is isn't it it'd it'll its it's itself i've j just k keep keeps kept
know known knows l last lately later latter latterly least less lest let let's
like liked likely likewise little look looking looks low lower ltd m made
mainly make makes many may maybe mayn't me mean meantime meanwhile merely
might mightn't mine minus miss more moreover most mostly mr mrs much must
mustn't my myself n name namely nd near nearly necessary need needn't needs
neither never neverf neverless nevertheless new next nine ninety no nobody non
none nonetheless noone no-one nor normally not nothing notwithstanding novel
now nowhere o obviously of off often oh ok okay old on once one ones one's
only onto opposite or other others otherwise ought oughtn't our ours ourselves
out outside over overall own p particular particularly past per perhaps placed
please plus possible presumably probably provided provides q que quite qv r
rather rd re really reasonably recent recently regarding regardless regards
relatively respectively right round s said same saw say saying says second
secondly see seeing seem seemed seeming seems seen self selves sensible sent
serious seriously seven several shall shan't she she'd she'll she's should
shouldn't since six so some somebody someday somehow someone something
sometime sometimes somewhat somewhere soon sorry specified specify specifying
still sub such sup sure t take taken taking tell tends th than thank thanks
thanx that that'll thats that's that've the their theirs them themselves then
thence there thereafter thereby there'd therefore therein there'll there're
theres there's thereupon there've these they they'd they'll they're they've
thing things think third thirty this thorough thoroughly those though three
through throughout thru thus till to together too took toward towards tried
tries truly try trying t's twice two u un under underneath undoing
unfortunately unless unlike unlikely until unto up upon upwards us use used
useful uses using usually v value various versus very via viz vs w want wants
was wasn't way we we'd welcome well we'll went were we're weren't we've what
whatever what'll what's what've when whence whenever where whereafter whereas
whereby wherein where's whereupon wherever whether which whichever while
whilst whither who who'd whoever whole who'll whom whomever who's whose why
will willing wish with within without wonder won't would wouldn't x y yes yet
you you'd you'll your you're yours yourself yourselves you've z zero
successful greatest began including being all for close but
""".split())

german_ignore = set("""aber als am an auch auf aus bei bin bis bist da dadurch daher darum das daß dass dein deine dem den der des dessen deshalb die dies dieser dieses doch dort du durch ein eine einem einen einer eines er es euer eure für hatte hatten hattest hattet hier     hinter ich ihr ihre im in ist ja jede jedem jeden jeder jedes jener jenes jetzt kann kannst können könnt machen mein meine mit muß mußt musst müssen müßt nach nachdem nein nicht nun oder seid sein seine sich sie sind soll sollen sollst sollt sonst soweit sowie und unser     unsere unter vom von vor wann warum was weiter weitere wenn wer werde werden werdet weshalb wie wieder wieso wir wird wirst wo woher wohin zu zum zur über aber alle allem allen aller alles als also am an ander andere anderem anderen anderer anderes anderm andern anderr anders auch auf aus bei bin bis bist da damit dann der den des dem die das daß dass derselbe derselben denselben desselben demselben dieselbe dieselben dasselbe dazu dein deine deinem deinen deiner deines denn derer dessen dich dir du dies diese diesem diesen dieser dieses doch dort durch ein eine einem einen einer eines einig einige einigem einigen einiger einiges einmal er ihn ihm es etwas euer eure eurem euren eurer eures für gegen gewesen hab habe haben hat hatte hatten hier hin hinter ich mich mir ihr ihre ihrem ihren ihrer ihres euch im in indem ins ist jede jedem jeden jeder jedes jene jenem jenen jener jenes jetzt kann kein keine keinem keinen keiner keines können könnte machen man manche manchem manchen mancher manches mein meine meinem meinen meiner meines mit muss musste nach nicht nichts noch nun nur ob oder ohne sehr sein seine seinem seinen seiner seines selbst sich sie ihnen sind so solche solchem solchen solcher solches soll sollte sondern sonst über um und uns unse unsem unsen unser unses unter viel vom von vor während war waren warst was weg weil weiter welche welchem welchen welcher welches wenn werde werden wie wieder will wir wird wirst wo wollen wollte würde würden zu zum zur zwar zwischen """.split()) 

__all__ = ["STOPWORDS"]
STOPWORDS = { 'en': english_ignore , 'de' : german_ignore}
