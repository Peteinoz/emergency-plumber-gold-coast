from _common import *

page = dict(
    slug="plumber-loganholme", kind="suburb", crumb="Plumber Loganholme",
    title="Plumber Loganholme | Homes & Hyperdome Area | Moyle",
    description='Plumber for Loganholme and Tanah Merah from Yatala: 1980s and 90s homes, stormwater, hot water, drains, gas and commercial. Call (07) 3807 7327.',
    h1="Plumber Loganholme",
    eyebrow="Loganholme QLD 4129",
    intro="<p>A plumber in Loganholme works across a suburb built mostly in the 1980s and 1990s, with the Logan River on one side and the Hyperdome's shops and offices on the other. Moyle Plumbing &amp; Gasfitting is a short run up the M1 from Yatala, and handles homes, rentals and businesses here with pricing agreed before we start.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Loganholme", area="Loganholme"),
    body=sec("""
<h2>A checklist for a 1980s or 90s Loganholme home</h2>
<ul class="checks">
<li><strong>Hot water:</strong> if the unit is original or a 2000s replacement, it is at or past the age where tanks fail. Have the valves checked and the age noted.</li>
<li><strong>Flexible hoses:</strong> anything installed during a kitchen or bathroom update in the 2000s is due now.</li>
<li><strong>Toilets:</strong> single-flush originals waste water and often seep; a dual-flush suite is a cheap upgrade.</li>
<li><strong>Tap bodies:</strong> worn seats and spindles cause the drips; reseating fixes most of them.</li>
<li><strong>Drains:</strong> gardens planted thirty years ago now have roots in the sewer. A camera check finds them before they block.</li>
<li><strong>Shower recess:</strong> original waterproofing may have failed; check for damp across the wall.</li>
<li><strong>Gas:</strong> flexible connectors and bayonets from the original install should be inspected.</li>
</ul>
<p>We can run through all of it in a single """ + L("general-plumbing-maintenance", "maintenance visit") + """ and hand you a list sorted into fine, do now and can wait.</p>
""") + soft("""
<h2>Low ground and the river</h2>
<p>Parts of Loganholme and Tanah Merah sit low near the Logan River, and it shows in the plumbing. Stormwater lines fill with silt, yard gullies overflow in heavy rain, and ground that stays wet corrodes buried pipes faster. Sewer lines in these streets are more prone to sagging as the ground moves. If your yard floods before the street does, or the sewer backs up during storms, the drains need a camera inspection rather than another clear. See """ + L("blocked-drains", "blocked drains") + """ and """ + L("leak-repairs", "leak detection") + """.</p>
""") + sec("""
<h2>Businesses around the Hyperdome</h2>
<p>The shops, cafes, offices and medical suites along Bryants Road and around the Hyperdome are commercial plumbing territory: grease traps, backflow testing, thermostatic mixing valves, commercial hot water and after-hours work so trading is not interrupted. That side of the business is described on the """ + L("commercial-plumbing", "commercial plumbing page") + """.</p>
<p>Anything urgent in Loganholme is handled the way the """ + H("Loganholme emergency plumber page") + """ home page sets out, including the valves and breakers to close first. Nearby """ + L("plumber-shailer-park", "Shailer Park") + """, """ + L("plumber-beenleigh", "Beenleigh") + """ and Eagleby are reached from the same depot. Toilet work is under """ + L("toilets", "toilets") + """ and leaking showers under """ + L("leaking-shower-repairs", "leaking shower repairs") + """. Moyle Plumbing has been one family's business through four decades; the background is on the """ + M("the family's main plumbing site") + """ site.</p>
""") + sec("""
<h2>Investment properties in Loganholme</h2>
<p>Loganholme has a strong rental market, and a good part of our work here comes from agencies managing 1980s and 90s houses and the townhouse complexes along the main roads. The typical work order is a hot water failure, a blocked sewer or a running cistern, and the typical question from the owner is whether to repair or replace. We answer that with photos and a set price for each option, so the property manager can get a decision without a second visit. Water efficiency compliance checks, which let owners pass on water charges, are often bundled into the same visit.</p>
"""),
    faqs=[
        ("Is Loganholme within your normal service area?",
         "<p>Yes. It is a few minutes north of Yatala up the highway and we are there most weeks.</p>"),
        ("My sewer backs up only when it rains. Why?",
         "<p>Stormwater is getting into the sewer somewhere, through a cracked pipe, a flooded overflow gully or an illegal connection, and overloading it. A camera inspection finds the entry point.</p>"),
        ("Can you convert my old electric hot water to a heat pump?",
         "<p>Usually yes, if there is space and airflow for the unit. We check the location, the electrical supply and any rebate available at the time before quoting.</p>"),
        ("Do you work on shops in the Hyperdome precinct?",
         "<p>Yes, including outside trading hours where the work would otherwise disrupt business.</p>"),
    ],
    related=[
        ("general-plumbing-maintenance", "Plumbing maintenance"),
        ("hot-water", "Hot water"),
        ("blocked-drains", "Blocked drains"),
        ("commercial-plumbing", "Commercial plumbing"),
        ("plumber-shailer-park", "Plumber Shailer Park"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
    ],
)
