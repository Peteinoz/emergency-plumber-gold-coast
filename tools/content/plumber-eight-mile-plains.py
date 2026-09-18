from _common import *

page = dict(
    slug="plumber-eight-mile-plains", kind="suburb", crumb="Plumber Eight Mile Plains",
    title="Plumber Eight Mile Plains | Brisbane Southside | Moyle",
    description="Plumber for Eight Mile Plains homes and townhouse complexes on Brisbane's southside. Hot water, drains, leaks and gas. Call (07) 3807 7327.",
    h1="Plumber Eight Mile Plains",
    eyebrow="Eight Mile Plains QLD 4113",
    intro="<p>A plumber in Eight Mile Plains meets two very different kinds of property in the same street: brick homes from the 1970s to 1990s on generous blocks, and the townhouse and unit complexes built since. Moyle Plumbing &amp; Gasfitting travels up the M1 from Yatala for both, and confirms the cost before any work begins.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Eight Mile Plains", area="Eight Mile Plains"),
    body=sec("""
<div class="two-col">
<div>
<h2>The established homes</h2>
<p>The original houses have the plumbing of their era: copper that is now pinholing, galvanised water services in the oldest streets, single-flush toilets, and sewer lines threaded through mature gardens. Hot water units on outside walls have been replaced once or twice already. The work is maintenance, replacement and the occasional renovation, and the priority is finding leaks before they get into brickwork and slabs.</p>
</div>
<div>
<h2>The complexes</h2>
<p>Townhouses and units bring body corporate boundaries, shared mains, common hot water plants in some buildings, and drainage that serves several lots. When something fails, the first question is whether it is lot or common property. We identify that on site and write the report so the committee or manager can act on it without another visit.</p>
</div>
</div>
""") + soft("""
<h2>What we are called for in Eight Mile Plains</h2>
""" + cards([
    ("hot-water", "Hot water", "Ageing storage units replaced, with slimline continuous flow or heat pump options for tight townhouse spaces."),
    ("leak-repairs", "Leak detection", "Slab and wall leaks in brick homes located with pressure testing and acoustic gear before anything is opened."),
    ("blocked-drains", "Blocked drains", "Roots in older lines, wipes in complex drains, cleared and camera-checked with footage supplied."),
    ("gas-fitting", "Gas", "Cooktop and hot water connections, leak repairs and compliance testing on natural gas streets."),
    ("bathroom-modifications", "Bathroom modifications", "Accessibility changes for owners staying in the family home as they get older."),
    ("commercial-plumbing", "Commercial", "Offices and businesses around the Logan Road and Garden City precinct."),
]) + """
""") + sec("""
<h2>Distance and scheduling</h2>
<p>Eight Mile Plains is at the northern end of our service area, so we usually group jobs on the southside into the same run. Booked maintenance is easy to schedule that way; for an urgent fault you get a truthful time estimate and the shut-off steps from the """ + H("southside emergency plumber page") + """. """ + L("plumber-rochedale-south", "Rochedale South") + """ next door and """ + L("plumber-shailer-park", "Shailer Park") + """ down the highway are covered on the same trip, as is hot water work across the """ + L("hot-water-repairs-brisbane-southside", "southside") + """. Moyle Plumbing &amp; Gasfitting is family owned and has traded since 1983; the full story is on """ + M("the Moyle Plumbing website") + """.</p>
""") + sec("""
<h2>Water pressure on the southside</h2>
<p>Unlike the Gold Coast estates, many Eight Mile Plains streets run at moderate pressure, and the complaint is more often too little than too much, particularly in the older houses. Low pressure at every tap usually means a corroded galvanised service or a meter tap not fully open; low pressure at one tap means a blocked aerator or a failing mixer. Where a whole-house pressure upgrade is needed, the fix is usually a new water service from the meter, which also ends the brown water after every council shutdown. In the townhouse complexes the opposite can be true, with booster pumps pushing pressure high enough to need limiting valves on each lot.</p>
"""),
    faqs=[
        ("Do you travel to Brisbane's southside for small jobs?",
         "<p>Yes, and it is more economical to group several small jobs into one visit. Tell us the list and we will price it as one job.</p>"),
        ("Who do I call in a townhouse when a shared pipe leaks?",
         "<p>Ring your body corporate manager and us. We locate the leak, work out whether it is lot or common property, stop it, and report so the cost can be allocated.</p>"),
        ("Can a heat pump fit a townhouse?",
         "<p>Often, if there is an outdoor space with airflow and the noise will not affect neighbours. Where it will not fit, a compact electric or instantaneous gas unit is the usual answer.</p>"),
        ("Is my 1980s copper likely to fail?",
         "<p>Copper of that age is at the point where pinholes appear, particularly on hot lines and where the pipe was in contact with concrete. A pressure test will show whether it is already losing water.</p>"),
    ],
    related=[
        ("hot-water", "Hot water"),
        ("leak-repairs", "Leak detection"),
        ("blocked-drains", "Blocked drains"),
        ("commercial-plumbing", "Commercial plumbing"),
        ("plumber-rochedale-south", "Plumber Rochedale South"),
        ("plumber-shailer-park", "Plumber Shailer Park"),
        ("hot-water-repairs-brisbane-southside", "Hot water repairs southside"),
    ],
)
