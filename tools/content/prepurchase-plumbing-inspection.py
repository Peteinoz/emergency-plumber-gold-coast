from _common import *

page = dict(
    slug="prepurchase-plumbing-inspection", kind="service", crumb="Pre-purchase inspection",
    title="Pre-Purchase Plumbing Inspection Gold Coast | Moyle",
    description='Pre-purchase plumbing inspection for homes on the northern Gold Coast, Logan and Redlands. Drains, pipes, hot water and gas. Call (07) 3807 7327.',
    h1="Pre-purchase plumbing inspection",
    eyebrow="Buying a home",
    intro="<p>A pre-purchase plumbing inspection looks at the parts of a house that a standard building report only glances at: the sewer, the water pipes, the hot water system and the gas installation. Moyle Plumbing &amp; Gasfitting inspects homes from the northern Gold Coast through Logan to the Redlands before contracts go unconditional, so you know what you are buying.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Pre-purchase plumbing inspection", area="Gold Coast"),
    body=sec("""
<h2>Why a building inspection is not enough</h2>
<p>Building and pest inspectors do valuable work, but they do not run a camera through the sewer, pressure test the water service or check that the gas installation has ever been certified. The most expensive plumbing faults in a house, a broken sewer under the slab, a leaking hot water line, a corroded water main, are exactly the ones that are invisible on the day of the open home.</p>
<h2>What we inspect</h2>
<ul class="checks">
<li><strong>Sewer and stormwater drains</strong> with a camera, looking for roots, cracks, sagging sections, collapsed pipe and illegal connections.</li>
<li><strong>Water service</strong> pressure tested from the meter, with a check for movement on the meter with all taps closed.</li>
<li><strong>Pipe materials</strong>, because galvanised, early poly and some copper is at the end of its useful life.</li>
<li><strong>Hot water system</strong> age, condition, valves, tempering, and whether the installation meets current requirements.</li>
<li><strong>Gas installation</strong> on properties with gas: leak test, appliance condition and flueing.</li>
<li><strong>Fixtures and taps</strong> for leaks, water efficiency and signs of past repairs.</li>
<li><strong>Wet areas</strong> for shower leaks, failed seals and water damage behind tiles where it can be detected.</li>
<li><strong>Tanks, pumps and septic</strong> on acreage properties, where they are the whole water and waste system.</li>
</ul>
""") + soft("""
<h2>What you get</h2>
<p>A plain-language written report with photos and drain camera footage, listing each item as fine, needs attention or needs repair, with a set price for any repairs you would like us to do after settlement. You can hand it to your solicitor, use it to negotiate, or simply plan the first year's maintenance.</p>
<p>We inspect with the agent's permission during the cooling-off or inspection period, and turn the report around promptly so you are not waiting on us to meet a deadline.</p>
""") + sec("""
<h2>Houses that most need it</h2>
<ul>
<li><strong>Older houses through Beenleigh, Loganholme, Springwood and Rochedale South</strong>, where original drains may be earthenware and water mains galvanised.</li>
<li><strong>Canal and waterfront homes in Hope Island and Helensvale</strong>, where pipework sits in damp, salty ground.</li>
<li><strong>Acreage in Mount Cotton, Alberton and Ormeau Hills</strong> on tank water, pumps and septic or treatment plants.</li>
<li><strong>Newer estate homes</strong>, where builder defects such as poorly glued drains or missing tempering valves show up after handover.</li>
<li><strong>Renovated homes</strong>, where it pays to confirm that plumbing and gas work was done by licensed trades and certified.</li>
</ul>
<p>Anything found can usually be fixed by the same team: """ + L("blocked-drains", "drain repairs") + """, """ + L("leak-repairs", "leak repairs") + """, """ + L("hot-water", "hot water replacement") + """ and """ + L("gas-fitting", "gas compliance work") + """. If you are already in the house and something has failed, the """ + H("emergency plumbing page") + """ page has the opening moves. We inspect across """ + L("plumber-beenleigh", "Beenleigh") + """, """ + L("plumber-helensvale", "Helensvale") + """, """ + L("plumber-redland-bay", "Redland Bay") + """ and the suburbs between. The company itself is at """ + M("www.moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Using the report</h2>
<p>Buyers use our reports three ways. Some negotiate: a sewer that needs relaying or a water service that needs replacing is a legitimate reason to revisit the price, and a written report with camera footage carries more weight than a verbal concern. Some walk away, which is the right call when the drainage under a slab has collapsed and the seller will not deal with it. Most simply plan: the report becomes the maintenance list for the first year, priced item by item, so nothing is a surprise once the keys are handed over. Whichever way you use it, the report is yours to share with your solicitor, your builder or the agent.</p>
"""),
    faqs=[
        ("How long does the inspection take?",
         "<p>Most houses take a couple of hours on site, longer for acreage properties with tanks and septic. The written report follows soon after.</p>"),
        ("Can I attend?",
         "<p>Yes, and it is worth doing. Seeing the drain footage and the hot water unit yourself makes the report easier to act on.</p>"),
        ("Do you inspect units and townhouses?",
         "<p>Yes. In a unit we focus on what belongs to the lot: fixtures, internal pipework, hot water and any gas, and note anything in the common property that is likely to become a levy issue.</p>"),
        ("Is the inspection worth it on a new house?",
         "<p>Often more than on an old one, because you are about to lose the builder's leverage. Drain camera footage plus a check of the hot water and gas paperwork catches defects while they can still be claimed.</p>"),
    ],
    related=[
        ("leak-repairs", "Leak detection"),
        ("blocked-drains", "Blocked drains"),
        ("hot-water", "Hot water systems"),
        ("gas-fitting", "Gas fitting"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
        ("plumber-helensvale", "Plumber Helensvale"),
        ("plumber-redland-bay", "Plumber Redland Bay"),
    ],
)
