from _common import *

page = dict(
    slug="general-plumbing-maintenance", kind="service", crumb="Plumbing maintenance",
    title="Home Plumbing Maintenance Gold Coast | Moyle Plumbing",
    description='Home plumbing maintenance across the northern Gold Coast, Beenleigh and Logan: taps, toilets, leaks, hot water and gas. Call (07) 3807 7327.',
    h1="Home plumbing maintenance, northern Gold Coast",
    eyebrow="Domestic maintenance",
    intro="<p>Home plumbing maintenance is the everyday work that keeps a house running: the dripping tap, the toilet that runs, the tap that squeals, the hose that should have been replaced two years ago. Moyle Plumbing &amp; Gasfitting has done this work from Yatala since 1983, for homeowners, landlords and property managers, at a price given before the job begins.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Domestic plumbing maintenance", area="Gold Coast"),
    body=sec("""
<h2>The jobs on a maintenance visit</h2>
<ul class="link-grid">
<li>Tap washers, spindles, ceramic cartridges and mixer bodies</li>
<li>Running, slow or leaking toilets</li>
<li>Replacing flexible hoses before they fail</li>
<li>Leaking shower heads, rails and roses</li>
<li>Noisy pipes and water hammer</li>
<li>Low or high water pressure</li>
<li>Washing machine and dishwasher taps</li>
<li>Garden taps, hose fittings and irrigation connections</li>
<li>Hot water valve and tempering valve checks</li>
<li>Gas appliance connections and cooktop swaps</li>
<li>Slow drains and floor wastes</li>
<li>Gutter downpipe connections and stormwater gullies</li>
</ul>
<p>Anything you have been meaning to get looked at can go on the same visit. It is cheaper to fix five small things in one call than to ring five times.</p>
""") + soft("""
<h2>A yearly once-over for the house</h2>
<p>Most plumbing disasters give warning. A maintenance check catches them while they are still cheap:</p>
<ol class="steps">
<li><strong>Flexible hoses</strong> under every basin, sink and toilet, looking for rust spots, bulges and kinks. These fail more often than any other part in a Gold Coast home.</li>
<li><strong>Water meter test</strong> with everything off, to find silent leaks before the water bill does.</li>
<li><strong>Hot water unit</strong>: relief valve operated, tempering valve checked, anode condition considered, age recorded.</li>
<li><strong>Toilets</strong>: cisterns checked for seepage, seals checked for movement.</li>
<li><strong>Pressure</strong> at the garden tap; too high shortens the life of every fixture.</li>
<li><strong>Gas</strong>: appliance flames, flexible connectors and isolation valves where the home has gas.</li>
<li><strong>Drains and gullies</strong>: overflow gully clear and gravel-free, floor wastes running freely.</li>
</ol>
<p>You get a short list: fine, fix now, can wait, with a set price for anything you want done.</p>
""") + sec("""
<h2>Older homes versus new estates</h2>
<p>In the older streets of Beenleigh, Loganholme and Eagleby the maintenance work is about ageing materials: galvanised water pipe, original taps, earthenware drains and hot water units past their best. In the newer estates of Pimpama, Coomera and Yarrabilba it is about builder shortcuts and high mains pressure: hoses that were the cheapest available, mixers failing early, and pressure limiting valves that were never fitted. We see both every week and carry parts for both.</p>
<p>Some maintenance jobs turn urgent when they are ignored. A weeping hose becomes a """ + L("burst-pipe", "burst pipe") + """; a slow drain becomes a """ + L("blocked-drains", "blocked sewer") + """; a dribbling relief valve becomes a failed """ + L("hot-water", "hot water unit") + """. When that has already happened, the """ + H("emergency plumber repair guide") + """ covers what to shut off first. Toilets have their own page under """ + L("toilets", "toilet repairs") + """, and kitchen work such as a new """ + L("dishwasher-installations", "dishwasher connection") + """ is common on a maintenance visit. We attend """ + L("plumber-ormeau", "Ormeau") + """, """ + L("plumber-beenleigh", "Beenleigh") + """ and """ + L("plumber-coomera", "Coomera") + """ most days. The full picture of the firm is at """ + M("moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Keeping a record</h2>
<p>A house has a service history the same way a car does, and most owners have no idea what theirs is. After each maintenance visit we leave a short note of what was replaced and when, including the hot water unit's age, the date the flexible hoses went in and the last time the drains were cleaned. Keep it with the house papers. It tells the next plumber, or the next owner, what has been done, and it stops the same part being replaced twice. For rentals, that record goes to the property manager and follows the property from tenancy to tenancy.</p>
"""),
    faqs=[
        ("Is it worth calling a plumber for one dripping tap?",
         "<p>Yes, though it is better value to gather up several small jobs for one visit. A dripping tap wastes a surprising amount of water over a year and usually means a washer or cartridge that takes minutes to replace.</p>"),
        ("Can you replace all the flexible hoses in the house?",
         "<p>Yes, and it is among the best preventive spends in the house. We fit quality braided hoses with isolation taps and note the date so you know when they are next due.</p>"),
        ("Do you do small gas jobs as well?",
         "<p>Yes. Connecting a new cooktop, replacing a bayonet fitting or checking a gas appliance can be done on the same visit as the plumbing work, because the business holds both licences.</p>"),
        ("How is maintenance work priced?",
         "<p>Every item is looked at and the list is priced as a whole before anything starts. You choose what goes ahead.</p>"),
    ],
    related=[
        ("toilets", "Toilet repairs"),
        ("leak-repairs", "Leak repairs"),
        ("hot-water", "Hot water systems"),
        ("blocked-drains", "Blocked drains"),
        ("dishwasher-installations", "Dishwasher installation"),
        ("plumber-ormeau", "Plumber Ormeau"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
        ("plumber-coomera", "Plumber Coomera"),
    ],
)
