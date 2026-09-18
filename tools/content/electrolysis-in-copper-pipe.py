from _common import *

page = dict(
    slug="electrolysis-in-copper-pipe", kind="post", crumb="Electrolysis in copper pipe",
    title="Electrolysis in Copper Pipe: Causes & Fixes | Moyle Plumbing",
    description='Electrolysis in copper pipe explained: why pinholes form from inside, what stray current and dissimilar metals do, and the fix. Call (07) 3807 7327.',
    h1="Electrolysis in copper pipe: why it fails from the inside",
    eyebrow="Handy hints",
    intro="<p>Electrolysis in copper pipe is the explanation for a leak that makes no sense: a pipe that looks fine on the outside, sprays water from a pinhole, and does it again a metre further along a few months later. This article explains what is happening inside the pipe, what causes it in Gold Coast and Logan homes, and how it is found and fixed.</p>",
    breadcrumb=[("handy-hints-blog", "Handy hints")],
    post=dict(published="2026-09-18", modified="2026-09-18"),
    body=sec("""
<h2>What electrolysis actually is</h2>
<p>Copper is a good conductor. When an electrical current passes along a copper pipe, or when copper is in contact with a different metal in the presence of water, a small electrochemical reaction takes place. Metal is lost from one surface, ion by ion. On a water pipe that loss happens on the inside, where the water is, so the first sign is not corrosion you can see but a pinhole that appears from nowhere.</p>
<p>Plumbers use "electrolysis" loosely to cover two related problems:</p>
<ul>
<li><strong>Stray current corrosion.</strong> Electricity flowing along the pipe because the pipe has become part of an electrical path. Older homes often used the copper water service as the earth for the switchboard, and a fault or a poor earth stake can push current through the pipework.</li>
<li><strong>Galvanic corrosion.</strong> Two different metals touching in water, such as copper joined directly to galvanised steel, or a brass fitting on steel. One metal sacrifices itself to the other.</li>
</ul>
""") + soft("""
<h2>How to recognise it</h2>
<ul class="checks">
<li>Pinhole leaks in copper that is otherwise in good condition, often several over a year or two.</li>
<li>Leaks that recur along the same run of pipe, usually the cold main or the first section from the meter.</li>
<li>Blue-green staining at the pinhole and, sometimes, a small raised blister on the outside of the pipe before it opens.</li>
<li>A copper pipe joined directly to galvanised steel somewhere in the system, with heavy corrosion right at the join.</li>
<li>A tingle from a tap, or the water pipe being used as the electrical earth. Both mean an electrician should look at the earthing.</li>
<li>Copper laid in contact with concrete or fill containing ash or salts, which speeds the reaction.</li>
</ul>
<p>Ordinary copper corrosion from aggressive water, and mechanical wear where a pipe rubs on a joist, can look similar. The pattern and the location usually tell them apart, and cutting out a failed section and looking at the inside confirms it.</p>
""") + sec("""
<h2>Fixing the cause, not just the hole</h2>
<ol class="steps">
<li><strong>Stop the current.</strong> If the pipe is carrying stray current, an electrician needs to correct the earthing so the plumbing is no longer part of the path. Repairing the pipe without this just moves the next pinhole along.</li>
<li><strong>Separate the metals.</strong> Where copper meets steel, a dielectric union or a length of plastic pipe breaks the galvanic cell.</li>
<li><strong>Replace the damaged run.</strong> Copper that has been losing metal for years is thin along its whole length, not just at the hole. Replacing the affected run, often in poly or PEX where it is buried, is more reliable than a series of patches.</li>
<li><strong>Keep copper off concrete and out of aggressive fill.</strong> Sleeving and correct bedding on any new run.</li>
</ol>
<h2>Where we see it</h2>
<p>Older houses around Beenleigh, Loganholme, Eagleby, Springwood and the first streets of Helensvale, where copper mains were laid decades ago and often joined to galvanised services, and where the pipe once served as the earth. It also turns up on hot water pipework where copper meets the steel connections on a tank. If your copper has started pinholing, a pressure test and an inspection of the exposed runs will show how far it has gone; see """ + L("leak-repairs", "leak detection and repair") + """ and """ + L("burst-pipe", "burst pipe repair") + """. Copper that has just let go is an emergency: turn off the meter and follow the """ + H("burst pipe emergency page") + """ steps. More reading is in the """ + L("frequently-asked-questions", "frequently asked questions") + """ article, and the people behind the article are on the """ + M("Moyle Plumbing website") + """.</p>
"""),
    faqs=[
        ("Can electrolysis affect plastic pipe?",
         "<p>No. Poly and PEX do not conduct and do not corrode, which is one reason they are used to replace affected copper runs.</p>"),
        ("Is my water safe if the copper is corroding?",
         "<p>The amount of copper entering the water is generally small, but blue-green staining on fixtures and a metallic taste are worth mentioning to us. Replacing the affected run resolves it.</p>"),
        ("Why does the electrician need to be involved?",
         "<p>Because the current causing the damage comes from the electrical system. Until the earthing is corrected, new copper will corrode the same way.</p>"),
        ("How do you confirm it is electrolysis and not just old pipe?",
         "<p>The pattern of failures, the presence of dissimilar metals or an earth connection, and the appearance of the pipe wall when a failed section is cut out. We show you what we find.</p>"),
    ],
    related=[
        ("leak-repairs", "Leak detection"),
        ("burst-pipe", "Burst pipe repair"),
        ("general-plumbing-maintenance", "Plumbing maintenance"),
        ("frequently-asked-questions", "Plumbing FAQs"),
        ("helpful-tips-for-plumbing-emergencies", "Emergency tips"),
        ("handy-hints-blog", "Handy hints"),
    ],
)
