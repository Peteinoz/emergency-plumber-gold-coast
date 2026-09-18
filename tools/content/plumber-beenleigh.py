from _common import *

page = dict(
    slug="plumber-beenleigh", kind="suburb", crumb="Plumber Beenleigh",
    title="Plumber Beenleigh | Moyle Plumbing & Gasfitting",
    description="Plumber for Beenleigh's older homes, rentals and shops, minutes from Yatala. Maintenance, hot water, drains, gas, inspections. Call (07) 3807 7327.",
    h1="Plumber Beenleigh",
    eyebrow="Beenleigh QLD 4207",
    intro="<p>A plumber in Beenleigh deals with some of the oldest housing on our patch. Weatherboard and brick homes from the 1960s to the 1980s sit alongside newer units and a busy town centre, and much of it is rented. Moyle Plumbing &amp; Gasfitting is a few minutes away at Yatala and has worked in Beenleigh since the business started in 1983.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Beenleigh", area="Beenleigh"),
    body=sec("""
<h2>Plumbing in Beenleigh's older homes</h2>
<p>Original plumbing from fifty years ago is still in service in many Beenleigh streets, and it is showing its age:</p>
<ul>
<li><strong>Galvanised steel water pipes</strong> that have rusted from the inside, reducing pressure to a trickle at the far taps and staining the water brown after a shutdown.</li>
<li><strong>Earthenware sewer drains</strong> with joints that roots have found, and sections that have cracked under decades of ground movement.</li>
<li><strong>Cast iron and copper</strong> in the older brick homes, corroding at the joints.</li>
<li><strong>Bathrooms on their original waterproofing</strong>, leaking into the wall next door.</li>
<li><strong>Hot water units</strong> in laundries and outside walls, on their third or fourth replacement.</li>
</ul>
<p>Replacing a galvanised water service with new pipe is one of the most satisfying jobs we do in the suburb: the pressure comes back and the discolouration stops. We price it as a set job after looking at the route.</p>
""") + soft("""
<h2>Rentals and shops</h2>
<p>A large proportion of Beenleigh homes are investment properties, and the town centre has shops, cafes and offices in older buildings. Property managers use us for maintenance, """ + L("water-compliancy", "water efficiency compliance") + """, hot water swaps and entry and exit checks, and we work to approval limits so owners are not surprised. For shops and offices, see """ + L("commercial-plumbing", "commercial plumbing") + """.</p>
<h2>Buying in Beenleigh?</h2>
<p>Older homes reward a proper look before you buy. A """ + L("prepurchase-plumbing-inspection", "pre-purchase plumbing inspection") + """ with the drains on camera and the water service under a pressure test tells you whether the price should allow for a new sewer or water main.</p>
""") + sec("""
<h2>Services in the suburb</h2>
<ul class="link-grid">
<li>""" + L("general-plumbing-maintenance", "General maintenance") + """</li>
<li>""" + L("hot-water", "Hot water") + """</li>
<li>""" + L("blocked-drains", "Drain clearing") + """</li>
<li>""" + L("leak-repairs", "Finding hidden leaks") + """</li>
<li>""" + L("gas-fitting", "Gas work") + """</li>
<li>""" + L("toilets", "Toilets") + """</li>
<li>""" + L("bathroom-renovations", "Bathroom renovations") + """</li>
<li>""" + L("emergency-plumber-beenleigh", "Emergency plumber Beenleigh") + """</li>
</ul>
<p>When something has already given way, follow the shut-off list on the """ + H("Beenleigh emergency plumbing page") + """ page before you ring. The urgent side of the suburb has its own page above. We cover neighbouring """ + L("plumber-loganholme", "Loganholme") + """, Eagleby and """ + L("plumber-ormeau", "Ormeau") + """ from the same base. Moyle Plumbing &amp; Gasfitting, family owned and licensed across plumbing and gas, has its history on the """ + M("Moyle Plumbing &amp; Gasfitting") + """ main site.</p>
""") + sec("""
<h2>Beenleigh's town centre and older commercial buildings</h2>
<p>Beenleigh's main street and the blocks around the station hold shops, pubs, offices and medical suites in buildings that have been refitted several times over the decades. The plumbing behind the walls often dates from the first fit-out: galvanised risers, cast iron stacks and drains that have been extended with each renovation. For tenants and landlords that means hot water plants that are worn out, backflow devices due for annual testing, and drainage that needs a camera before any new fit-out is planned. We handle that commercial work alongside the residential, and because the depot is minutes away, a blocked drain in a packed cafe can usually be attended without the shop closing for the day.</p>
"""),
    faqs=[
        ("Why is my water brown after the council turned it off?",
         "<p>Rust inside galvanised pipes gets disturbed when flow stops and restarts. It is a sign the pipes are corroding and will eventually need replacing.</p>"),
        ("Can old earthenware drains be repaired rather than replaced?",
         "<p>Often a single cracked section can be dug and replaced while the rest is left in service. A camera inspection shows how much of the line is affected before we quote.</p>"),
        ("Do you work with Beenleigh property managers?",
         "<p>Yes. Send the work order, we contact the tenant, do the job within the approval limit and report the cause.</p>"),
        ("How close are you to Beenleigh?",
         "<p>Yatala is the next suburb. Beenleigh is one of the quickest areas for us to reach.</p>"),
    ],
    related=[
        ("emergency-plumber-beenleigh", "Emergency plumber Beenleigh"),
        ("hot-water", "Hot water"),
        ("blocked-drains", "Blocked drains"),
        ("prepurchase-plumbing-inspection", "Pre-purchase inspections"),
        ("real-estate-property-manager", "Property managers"),
        ("plumber-loganholme", "Plumber Loganholme"),
        ("plumber-ormeau", "Plumber Ormeau"),
    ],
)
