from _common import *

page = dict(
    slug="water-compliancy", kind="service", crumb="Water compliance",
    title="Water Efficiency Compliance for QLD Rentals | Moyle Plumbing",
    description='Water efficiency compliance checks and documentation for Queensland rentals on the northern Gold Coast and Logan. Call (07) 3807 7327.',
    h1="Water efficiency compliance for Queensland rentals",
    eyebrow="Rental compliance",
    intro="<p>Water efficiency compliance decides whether a Queensland landlord can pass water consumption charges on to the tenant. The property has to be individually metered, free of leaks and fitted with water-efficient fixtures, and the owner needs evidence. Moyle Plumbing &amp; Gasfitting inspects, fixes and documents rentals across the northern Gold Coast and Logan.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Water efficiency compliance inspections", area="Gold Coast"),
    body=sec("""
<h2>What the rules require</h2>
<p>Under Queensland tenancy law, an owner can charge a tenant for all water consumption only when the premises meet all of these:</p>
<ul class="checks">
<li>The property is individually metered, or water is delivered by a supplier and separately measured.</li>
<li>The tenancy agreement states that the tenant pays for water consumption.</li>
<li>The premises are water efficient: internal cold water taps and shower heads have a maximum flow of 9 litres per minute, and toilets are dual flush with a full flush of no more than 6.5 litres and a half flush of no more than 3.5 litres.</li>
<li>There are no leaking taps or toilets at the start of the tenancy and whenever the fixtures are checked.</li>
</ul>
<p>The efficiency requirements apply to internal fixtures. Garden taps, bath outlets and laundry machine taps are not part of the flow-rate test.</p>
""") + soft("""
<h2>What our compliance visit covers</h2>
<ol class="steps">
<li>Flow test every internal cold tap and shower head with a calibrated measure, and record the result.</li>
<li>Check each toilet for dual flush and for seepage from cistern to bowl.</li>
<li>Check all fixtures for drips and leaks, including the hot water relief valve and any visible pipework.</li>
<li>Fit flow restrictors, aerators or efficient shower heads where a fixture fails, with your approval, at a set price told to you first.</li>
<li>Replace washers, cartridges or cistern parts to stop leaks.</li>
<li>Issue documentation listing each fixture, its flow rate and the date, for the property manager's file.</li>
</ol>
""") + sec("""
<h2>Why it pays even without a tenant paying water</h2>
<p>Efficient fixtures cut the water bill whoever pays it, and a leak check finds the running toilet that is costing more than the plumber. For managed properties we can combine the compliance check with an entry or exit condition inspection, a """ + L("hot-water-tempering-valves", "tempering valve check") + """ or a hot water service, so the owner pays for one visit. Our work with agencies is described on the """ + L("real-estate-property-manager", "property manager page") + """.</p>
<h2>Common failures we see</h2>
<ul>
<li>Older single-flush toilets in original bathrooms; a new dual-flush suite is the fix. See """ + L("toilets", "toilet replacement") + """.</li>
<li>Kitchen mixers with no aerator, flowing well over the limit.</li>
<li>Shower heads swapped by a previous tenant for a high-flow model.</li>
<li>Cistern outlet washers seeping, which fails the leak test even though nobody has noticed.</li>
<li>Hidden leaks showing on the meter, which we trace under """ + L("leak-repairs", "leak detection") + """.</li>
</ul>
<p>Compliance checks are booked work, but tenants sometimes report a leak that has turned into a flood on the same day; the """ + H("emergency plumber for rentals") + """ page covers what to tell them to shut off. We do compliance visits in """ + L("plumber-beenleigh", "Beenleigh") + """, """ + L("yarrabilba-plumber", "Yarrabilba") + """, """ + L("plumber-coomera", "Coomera") + """ and the suburbs around them. Full company details are on """ + M("the Moyle Plumbing home site") + """.</p>
""") + sec("""
<h2>Shower heads, tenants and the flow test</h2>
<p>The fixture that most often fails a compliance check is the shower head, and usually not the one the owner installed. Tenants swap efficient heads for high-flow models and take them when they leave, or leave them behind. Because the requirement applies at the start of each tenancy, a property can pass one year and fail the next without the owner changing anything. The practical answer is a flow test at each changeover and a spare efficient head kept on file with the agency. The same goes for aerators, which are cheap, easily removed and easily forgotten.</p>
"""),
    faqs=[
        ("Is a water efficiency certificate a legal document?",
         "<p>There is no prescribed government certificate. What matters is evidence that the fixtures met the requirements at the relevant time. Our report records the flow rates and toilet types with the date, which is what tribunals and tenants ask for.</p>"),
        ("Does the check need repeating for each new tenancy?",
         "<p>The property must be efficient and leak-free at the start of each tenancy. Many agencies have fixtures rechecked at each changeover or at least periodically, since tenants swap shower heads and washers wear.</p>"),
        ("What if the toilet is single flush?",
         "<p>It fails the requirement. Replacing it with a dual-flush suite is usually the only fix, and we can do it on the same visit if approved.</p>"),
        ("Can you fix the failures on the spot?",
         "<p>Yes, with approval. We carry aerators, restrictors, efficient shower heads and common tap and cistern parts, and price the work before doing it.</p>"),
    ],
    related=[
        ("real-estate-property-manager", "Property managers"),
        ("hot-water-tempering-valves", "Tempering valves"),
        ("toilets", "Toilet replacement"),
        ("leak-repairs", "Leak detection"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
        ("yarrabilba-plumber", "Plumber Yarrabilba"),
        ("plumber-coomera", "Plumber Coomera"),
    ],
)
