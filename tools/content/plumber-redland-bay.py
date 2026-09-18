from _common import *

page = dict(
    slug="plumber-redland-bay", kind="suburb", crumb="Plumber Redland Bay",
    title="Plumber Redland Bay | Bayside & Acreage | Moyle Plumbing",
    description="Plumber for Redland Bay's older bayside homes, new estates and acreage from Yatala. Hot water, drains, leaks, gas and pumps. Call (07) 3807 7327.",
    h1="Plumber Redland Bay",
    eyebrow="Redland Bay QLD 4165",
    intro="<p>A plumber in Redland Bay sees three kinds of property in a single day: older homes near the water, new estate houses on the western side, and acreage blocks on tanks. Moyle Plumbing &amp; Gasfitting drives over from Yatala for all three, and sets the cost before anything begins.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Redland Bay", area="Redland Bay"),
    body=sec("""
<h2>Three kinds of Redland Bay property</h2>
<ol class="steps">
<li><strong>The older homes near the bay.</strong> Beach houses and post-war cottages that have grown over the decades, with plumbing from several eras joined together. Salt air and damp ground shorten the life of buried and exposed metal pipe, and drains have often been extended in ways nobody documented. Camera inspection is worth it before any work on the sewer.</li>
<li><strong>The new estates.</strong> Homes built in the last decade or two with PVC drains, high mains pressure and builder-grade fittings. The first round of hot water and hose replacements is arriving, and a pressure limiting valve prevents a lot of it.</li>
<li><strong>Acreage and semi-rural blocks.</strong> Tank water, pumps, filtration and septic or treatment plants, plus sheds and second dwellings that need water and drainage. See """ + L("pumps", "pumps") + """.</li>
</ol>
""") + soft("""
<h2>Work we do here</h2>
<ul class="link-grid">
<li>""" + L("hot-water", "Hot water repairs and replacement") + """</li>
<li>""" + L("blocked-drains", "Drains and sewer blockages") + """</li>
<li>""" + L("leak-repairs", "Leak tracing") + """</li>
<li>""" + L("gas-fitting", "LPG and natural gas") + """</li>
<li>""" + L("general-plumbing-maintenance", "Maintenance") + """</li>
<li>""" + L("prepurchase-plumbing-inspection", "Pre-purchase inspections") + """</li>
<li>""" + L("bathroom-renovations", "Bathroom renovations") + """</li>
<li>""" + L("water-filter-installation", "Tank water filtration") + """</li>
</ul>
<p>Buying near the bay? Older homes here are a strong case for a pre-purchase plumbing inspection, because the drains and water service may be older than the current house and the sale price should reflect what they need.</p>
""") + sec("""
<h2>Getting to Redland Bay</h2>
<p>We come across from Yatala through Mount Cotton, and usually group Redlands jobs on the same day. Booked work is easy to fit in; for a fault that cannot wait, isolate first using the """ + H("emergency plumber Gold Coast and Redlands") + """ page then ring """ + PHONE + """, and you will get an honest arrival estimate. """ + L("plumber-mount-cotton", "Mount Cotton") + """ is on the way, and the same acreage skills apply on both sides of the boundary. Moyle Plumbing &amp; Gasfitting has remained a family business since 1983, and its details are on """ + M("moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Storm season on the bay</h2>
<p>Redland Bay cops the weather off Moreton Bay, and the plumbing that suffers is on the outside of the house: gutters and downpipes overwhelmed by a summer storm, stormwater pits full of leaf litter, garden mains cracked by movement in wet ground, and hot water units on exposed walls rusting faster than they should. A pre-summer check of the stormwater and the outside plumbing is worth more here than in most suburbs. For the acreage blocks, that check includes the tank overflow and the first-flush diverter, because a blocked diverter sends the dirtiest water of the year straight into the tank.</p>
<h2>Working with Redlands agencies</h2>
<p>Property managers in the Redlands send us maintenance, hot water and compliance work, and we run it the same way as everywhere else: tenant contact direct, approval limits respected, photos and cause noted on the invoice.</p>
"""),
    faqs=[
        ("Is Redland Bay in your service area?",
         "<p>Yes. It is at the eastern edge of the area we cover, reached through Mount Cotton from Yatala.</p>"),
        ("Why do exposed pipes corrode faster near the bay?",
         "<p>Salt in the air attacks copper, brass and steel. Fittings on outside walls, hot water units and garden taps show it first. Replacing with suitable materials and keeping fittings out of the weather helps.</p>"),
        ("Can you work on a house on tank water and septic?",
         "<p>Yes. Pumps, filtration, septic drains and treatment plant plumbing are everyday work for us in the Redlands and around Yatala.</p>"),
        ("Do you service the bay islands?",
         "<p>Our work is on the mainland. For a property outside the usual area, ring and ask; you will get a straight answer.</p>"),
    ],
    related=[
        ("hot-water", "Hot water"),
        ("blocked-drains", "Blocked drains"),
        ("leak-repairs", "Leak detection"),
        ("pumps", "Pumps"),
        ("prepurchase-plumbing-inspection", "Pre-purchase inspections"),
        ("plumber-mount-cotton", "Plumber Mount Cotton"),
    ],
)
