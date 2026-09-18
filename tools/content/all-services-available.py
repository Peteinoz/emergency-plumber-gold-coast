from _common import *

page = dict(
    slug="all-services-available", kind="hub", crumb="Services",
    title="Plumbing Services Gold Coast | All Services | Moyle",
    description='Every plumbing and gas service from Moyle Plumbing & Gasfitting across the northern Gold Coast, Beenleigh, Logan and Brisbane. Call (07) 3807 7327.',
    h1="Plumbing services on the Gold Coast: everything we do",
    eyebrow="Services hub",
    intro="<p>These are the plumbing services Moyle Plumbing &amp; Gasfitting provides from Yatala across the northern Gold Coast, Beenleigh, Logan and Brisbane's southside. Domestic, commercial and real estate work, plumbing and gas under one licence, with the price given before any job starts. Pick the page that matches your problem.</p>",
    breadcrumb=[],
    body=sec("""
<h2>Urgent and repair work</h2>
""" + cards([
    ("emergency-plumbing", "Emergency plumbing", "What counts as an emergency, how a callout runs and what to isolate before we arrive."),
    ("burst-pipe", "Burst pipe repair", "Failed copper, poly and flexible hoses found, repaired and tested."),
    ("blocked-drains", "Blocked drains", "Sewer, kitchen, bathroom and stormwater blockages cleared with jetting, cable and camera."),
    ("leak-repairs", "Leak detection and repair", "Concealed leaks under slabs, in walls and in gardens found with test equipment before any digging."),
    ("toilets", "Toilet repairs and replacement", "Running cisterns, blocked pans, leaking seals and new suites."),
    ("leaking-shower-repairs", "Leaking shower repairs", "Tests that tell a pipe fault from failed waterproofing, then the right fix."),
]) + """
<h2>Hot water and gas</h2>
""" + cards([
    ("hot-water", "Hot water systems", "Repair and replacement across every fuel type."),
    ("hot-water-tempering-valves", "Tempering valves", "The scald-protection valve on every hot water system, tested and replaced."),
    ("gas-fitting", "Gas fitting", "Leaks, appliance connections, hot water and compliance testing by licensed gasfitters."),
    ("bbq-gas-bottle", "BBQ gas connections", "Bayonet points and LPG bottle installations for outdoor cooking."),
]) + """
<h2>Everyday and kitchen plumbing</h2>
""" + cards([
    ("general-plumbing-maintenance", "Plumbing maintenance", "Taps, hoses, pressure, small leaks and the yearly once-over that prevents the big failures."),
    ("dishwasher-installations", "Dishwasher installation", "New points, isolation taps and leak-safe connections."),
    ("insinkerator", "InSinkErator installation", "Food waste disposers fitted and replaced with correct sink and drain connections."),
    ("water-filter-installation", "Water filter installation", "Under-sink, whole-house and tank water filtration."),
    ("pumps", "Pumps", "Tank pressure pumps, sump pumps, sewage pumps and macerators repaired and installed."),
]) + """
<h2>Bathrooms and renovations</h2>
""" + cards([
    ("bathroom-renovations", "Bathroom renovation plumbing", "Rough-in, drainage changes and fit-off, working with your builder."),
    ("bathroom-modifications", "Bathroom modifications", "Accessibility changes: walk-in showers, raised toilets, lever taps, scald protection."),
]) + """
<h2>Property, compliance and commercial</h2>
""" + cards([
    ("real-estate-property-manager", "Property managers and rentals", "Work orders, tenant contact, approval limits and clear reporting."),
    ("water-compliancy", "Water efficiency compliance", "Flow testing and documentation so Queensland landlords can pass on water charges."),
    ("prepurchase-plumbing-inspection", "Pre-purchase plumbing inspection", "Drains, pipes, hot water and gas checked before you buy."),
    ("commercial-plumbing", "Commercial plumbing", "Shops, cafes, workshops, schools and body corporates."),
    ("environmental-green-plumbers", "Water and energy efficient plumbing", "Cutting water and energy use through fixture choice and hot water selection."),
]) + """
""") + soft("""
<h2>Where these services are available</h2>
<p>All of the above is offered across the suburbs on the """ + L("suburbs-serviced", "suburbs serviced page") + """: the northern Gold Coast from Ormeau to Helensvale, Beenleigh and Logan, Brisbane's southside, and the acreage country out towards Mount Cotton and the Redlands. If the job is urgent, start with the """ + H("emergency plumber near me") + """ home page, which sets out what to isolate first and how a callout is priced. Questions about the business itself are answered on the """ + L("about-us", "about page") + """, and you can also read about """ + M("Moyle Plumbing &amp; Gasfitting") + """ on its main website.</p>
"""),
    faqs=[
        ("Do you do both plumbing and gas work?",
         "<p>Yes. Both licences are held, so a gas hot water fault or a kitchen with a gas cooktop and a dishwasher can be handled in one visit.</p>"),
        ("How is a job priced?",
         "<p>The plumber finds the fault and quotes one fixed figure before starting. Surprises once the job is open are discussed with you before they are dealt with.</p>"),
        ("Is there a service you do not offer?",
         "<p>We do not do tiling, waterproofing or electrical work ourselves, though we coordinate with those trades on renovations and hot water installs. Ring us if you are unsure whether a job is ours.</p>"),
    ],
    related=[
        ("suburbs-serviced", "Suburbs serviced"),
        ("about-us", "About us"),
        ("contact-us", "Contact"),
        ("handy-hints-blog", "Handy hints"),
    ],
)
