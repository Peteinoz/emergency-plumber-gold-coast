from _common import *

page = dict(
    slug="toilets", kind="service", crumb="Toilets",
    title="Toilet Repairs & Replacement Gold Coast | Moyle Plumbing",
    description='Toilet repairs and replacement across the northern Gold Coast, Beenleigh and Logan. Running cisterns, blocked pans, new suites. Call (07) 3807 7327.',
    h1="Toilet repairs and replacement",
    eyebrow="Toilets",
    intro="<p>Toilet repairs and replacement sound minor until the household's one toilet stops working. Moyle Plumbing &amp; Gasfitting fixes running cisterns, blocked pans, leaking pan seals and failed inlet valves across the northern Gold Coast, and replaces whole suites when repair no longer makes sense. You know the price before we start.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Toilet repair and replacement", area="Gold Coast"),
    body=sec("""
<h2>Common toilet faults and what they mean</h2>
<table>
<thead><tr><th>Symptom</th><th>Probable cause</th><th>Urgency</th></tr></thead>
<tbody>
<tr><td>Cistern runs constantly or hisses</td><td>Worn inlet valve or outlet washer</td><td>Soon: it wastes a lot of water</td></tr>
<tr><td>Water on the floor around the base</td><td>Failed pan seal or cracked pan</td><td>Soon: it is sewage, not clean water</td></tr>
<tr><td>Weak or partial flush</td><td>Blocked rim jets, wrong water level, worn flush valve</td><td>Book it</td></tr>
<tr><td>Bowl fills and drains slowly</td><td>Partial blockage in the pan or branch</td><td>Book it, or urgent if it is the only toilet</td></tr>
<tr><td>Overflows when flushed</td><td>Full blockage</td><td>Urgent: stop flushing and call</td></tr>
<tr><td>Gurgles when the shower drains</td><td>Main drain restriction</td><td>Urgent if worsening: see """ + L("blocked-drains", "blocked drains") + """</td></tr>
</tbody>
</table>
<h2>Blocked toilet: what to do first</h2>
<p>Do not keep flushing. If the water is high in the bowl, wait for it to drop, then try a proper toilet plunger with a flange, with a few firm pushes. If it does not clear after that, leave it. Chemical drain cleaners do nothing for a toilet blockage and make the job unpleasant and unsafe for the plumber. If sewage is surfacing at the outside gully, the problem is the main line rather than the toilet.</p>
""") + soft("""
<h2>Repair or replace the suite?</h2>
<p>Most faults are cheap to fix: an inlet valve, an outlet washer, a new flush button or a pan seal. Replacement is the better call when:</p>
<ul>
<li>The pan or cistern is cracked. Hairline cracks in porcelain do not stay hairline.</li>
<li>Parts for an old or obscure cistern are no longer made.</li>
<li>It is a single-flush unit and you want to cut water use, or need a dual-flush suite for a """ + L("water-compliancy", "water compliant rental") + """.</li>
<li>The bathroom is being modified for someone with limited mobility and a taller or wall-faced pan would help. See """ + L("bathroom-modifications", "bathroom modifications") + """.</li>
</ul>
<p>We supply and fit new suites, including back-to-wall, close-coupled and concealed cistern designs, and match the outlet position to your existing drain so the floor does not need to come up.</p>
""") + sec("""
<h2>Water waste from toilets</h2>
<p>A cistern that runs quietly can lose more water than a dripping tap. The simple check: put a few drops of food colouring in the cistern and wait ten minutes without flushing. Colour in the bowl means the outlet washer is passing and needs replacing. Older single-flush cisterns also use far more water per flush than a modern dual-flush, which is why property managers and owners often replace them at the same time as fixing a fault.</p>
<p>Toilet work is part of everyday """ + L("general-plumbing-maintenance", "plumbing maintenance") + """, but an overflowing pan in a one-bathroom home is exactly what the """ + H("overflowing toilet emergency page") + """ page is for. A leak around the base can also be traced under """ + L("leak-repairs", "leak repairs") + """ if the source is unclear. Family owned since 1983, """ + M("our Yatala plumbing team's main site") + """ works from Yatala across Loganholme, Ormeau and the northern Gold Coast.</p>
""") + sec("""
<h2>Concealed cisterns and wall-hung pans</h2>
<p>Renovated bathrooms across the northern Gold Coast increasingly use in-wall cisterns with a flush plate and a wall-hung pan. They look clean and are easy to mop under, but they need the right frame installed before the wall is sheeted, and when a part fails the repair goes through the flush plate opening. We install the frames during renovations and carry the common inlet and flush valve parts for the major brands, so a running concealed cistern does not mean opening the wall. If you are planning one, tell us early so the frame and the drain position are right the first time.</p>
"""),
    faqs=[
        ("Why does my toilet keep running after flushing?",
         "<p>Usually the outlet washer or flapper is worn and lets water seep into the bowl, so the inlet valve keeps topping up. Sometimes the float is set too high and water runs over the overflow. Both are quick repairs.</p>"),
        ("Can you replace just the cistern?",
         "<p>Often, if a compatible cistern is available for the pan. On older suites the pan and cistern are matched, and a full suite is more reliable and not much dearer.</p>"),
        ("How long does a toilet replacement take?",
         "<p>A simple swap with the drain and water in the usual positions is normally one visit. If the floor outlet needs moving or the wall needs work, we tell you before starting.</p>"),
        ("What should never go down the toilet?",
         "<p>Wipes of any kind, sanitary products, cotton buds, paper towel, dental floss and food. Only toilet paper breaks down quickly enough for the drain.</p>"),
    ],
    related=[
        ("blocked-drains", "Blocked drains"),
        ("leak-repairs", "Leak repairs"),
        ("bathroom-modifications", "Bathroom modifications"),
        ("water-compliancy", "Water compliance"),
        ("plumber-loganholme", "Plumber Loganholme"),
        ("plumber-ormeau", "Plumber Ormeau"),
    ],
)
