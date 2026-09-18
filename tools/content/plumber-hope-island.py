from _common import *

page = dict(
    slug="plumber-hope-island", kind="suburb", crumb="Plumber Hope Island",
    title="Plumber Hope Island | Canal & Resort Homes | Moyle",
    description="Plumber for Hope Island's canal, golf and gated estates from Yatala. Quality fixtures, discreet work, set pricing. Call (07) 3807 7327.",
    h1="Plumber Hope Island",
    eyebrow="Hope Island QLD 4212",
    intro="<p>A plumber in Hope Island needs to be comfortable with gatehouses, body corporate rules, premium tapware and pipework that sits in salty, waterlogged ground. Moyle Plumbing &amp; Gasfitting has worked in the canal and golf estates of Hope Island for years from its base at Yatala, and prices every job before starting.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Hope Island", area="Hope Island"),
    body=sec("""
<h2>Five things that are different about plumbing in Hope Island</h2>
<ol class="steps">
<li><strong>The ground.</strong> Reclaimed and canal-edge land holds water and salt. Buried copper and steel corrode faster, and pipe joints in the yard move as the ground settles. Yard leaks are more common here than in suburbs on higher ground.</li>
<li><strong>The fixtures.</strong> Homes are fitted with designer mixers, rain showers, in-wall cisterns and outdoor showers. Parts are brand-specific and we make sure we have the right ones before opening a wall.</li>
<li><strong>Access.</strong> Gated estates and resort precincts have entry procedures and working-hour rules. We arrange access ahead of time so the visit is not spent at the gate.</li>
<li><strong>Body corporate.</strong> Many properties are in schemes where the boundary between lot and common plumbing matters for who pays. We identify which side the fault is on and write it up accordingly.</li>
<li><strong>Outdoor living.</strong> Pontoons, pool areas and outdoor kitchens mean extra taps, gas bayonets and drains, all exposed to weather and salt.</li>
</ol>
""") + soft("""
<h2>Work we are asked for most</h2>
""" + cards([
    ("leak-repairs", "Leak detection", "Locating leaks under slabs, in garden mains and behind tiled walls before anything is opened."),
    ("hot-water", "Hot water", "Systems sized for several bathrooms, continuous flow banks and heat pumps sited where the noise will not bother anyone."),
    ("bathroom-renovations", "Renovation plumbing", "Rough-in and fit-off for high-end bathroom and kitchen refits, working with designers and builders."),
    ("gas-fitting", "Gas", "Outdoor kitchens, pool heaters and bayonets for entertaining areas."),
    ("dishwasher-installations", "Kitchen appliances", "Integrated dishwashers, filtered water taps and waste disposers connected correctly."),
    ("general-plumbing-maintenance", "Maintenance", "Premium fixtures serviced with the right parts, not generic substitutes."),
]) + """
""") + sec("""
<h2>Discreet and tidy</h2>
<p>Much of our Hope Island work is in occupied homes with fine finishes. Drop sheets go down, boots come off or get covered, and the work area is left clean. If a wall has to be opened we do it from the least visible side and keep the opening as small as the repair allows.</p>
<p>For a burst hose or a leak that is running now, close the meter or the lot valve and follow the """ + H("Hope Island emergency plumber steps") + """ page. We get to Hope Island via the M1 and Hope Island Road from Yatala, and cover neighbouring """ + L("plumber-coomera", "Coomera") + """ and """ + L("plumber-helensvale", "Helensvale") + """ on the same run. Family owned since 1983 and licensed for plumbing and gas, """ + M("Moyle Plumbing") + """ has more on its main site.</p>
""") + sec("""
<h2>Absentee owners</h2>
<p>A good many Hope Island homes are second homes or investment properties, with the owner interstate or overseas. That changes how we work: photos before and after, a written description of the fault and the fix, approval by email against a set price, and liaison with the estate management or the caretaker for access. For properties left empty for months, a pre-departure check that closes the water at the meter and isolates the hot water unit is cheap insurance against coming back to a flooded house, and we can do it as part of a routine maintenance visit.</p>
"""),
    faqs=[
        ("Can you get parts for my imported tapware?",
         "<p>Usually. We identify the brand and model first, source the cartridge or part, and book the repair once it is in hand, so the wall is only opened once.</p>"),
        ("Who pays for a leak in a body corporate building?",
         "<p>It depends on whether the pipe serves only your lot or is common property. We locate the leak, identify which side of the boundary it sits on and report it so the committee can decide quickly.</p>"),
        ("Do you deal with the estate gatehouse?",
         "<p>Yes. Give us the estate's contractor procedure when you book and we will arrange entry in advance.</p>"),
        ("My garden is always wet in one spot. Is it a leak?",
         "<p>On Hope Island it often is, because buried pipes corrode in the salty ground. A meter test and leak detection will confirm it before any digging.</p>"),
    ],
    related=[
        ("leak-repairs", "Leak detection"),
        ("hot-water", "Hot water"),
        ("bathroom-renovations", "Bathroom renovations"),
        ("gas-fitting", "Gas fitting"),
        ("plumber-coomera", "Plumber Coomera"),
        ("plumber-helensvale", "Plumber Helensvale"),
    ],
)
