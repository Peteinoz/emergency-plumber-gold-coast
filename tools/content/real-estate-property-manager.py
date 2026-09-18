from _common import *

page = dict(
    slug="real-estate-property-manager", kind="service", crumb="Property managers",
    title="Plumber for Property Managers & Rentals | Moyle Plumbing",
    description='Plumber for property managers and rentals across the northern Gold Coast, Beenleigh and Logan. Fast reporting, set pricing. Call (07) 3807 7327.',
    h1="Plumber for property managers and rental properties",
    eyebrow="Real estate",
    intro="<p>A plumber for property managers needs to do three things well: get to the tenant, fix it properly at a price the owner will accept, and send back a clear report. Moyle Plumbing &amp; Gasfitting has partnered with agencies around the northern Gold Coast, Beenleigh and Logan for years and built its process around exactly that.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Real estate and property manager plumbing", area="Gold Coast"),
    body=sec("""
<h2>How a work order runs with us</h2>
<ol class="steps">
<li><strong>Send the work order</strong> by email to """ + MAILTO + """ or ring """ + PHONE + """ for anything urgent. Include the tenant's contact details and any access notes.</li>
<li><strong>We contact the tenant directly</strong> to arrange access, so you are not the go-between.</li>
<li><strong>On site,</strong> the plumber diagnoses the fault and, for anything beyond the agreed limit, sends you a set price for approval before proceeding.</li>
<li><strong>Repair and report.</strong> You receive the invoice with a description of the cause, photos where useful, and a note on whether it looks like wear or misuse.</li>
</ol>
<p>Set pricing means an owner can approve work knowing the figure will not move unless something genuinely unexpected turns up, and in that case you hear first.</p>
""") + soft("""
<h2>Rental work we handle</h2>
<ul class="cards cols-2">
<li class="card"><h3>""" + L("emergency-plumbing", "Emergency repairs") + """</h3><p>Burst pipes, no hot water, blocked sewers and gas smells, attended with the same-day aim on genuine emergencies so your tenant is not left without essentials.</p></li>
<li class="card"><h3>""" + L("water-compliancy", "Water efficiency compliance") + """</h3><p>Checks and certificates that allow owners to pass on water consumption charges under Queensland tenancy law, with efficient fixtures fitted where needed.</p></li>
<li class="card"><h3>""" + L("hot-water", "Hot water systems") + """</h3><p>Repairs, replacements and """ + L("hot-water-tempering-valves", "tempering valve") + """ checks, with photos of the unit and its compliance plate for the file.</p></li>
<li class="card"><h3>""" + L("blocked-drains", "Blocked drains") + """</h3><p>Cleared with a report on the cause, which matters when deciding whether the tenant or owner bears the cost.</p></li>
<li class="card"><h3>Entry and exit condition checks</h3><p>Plumbing checked between tenancies: taps, toilets, hot water, drains and any sign of leaks, so problems are recorded before the next tenant moves in.</p></li>
<li class="card"><h3>General maintenance</h3><p>Dripping taps, running cisterns, leaking showers, broken toilet seats and the small items that keep tenants happy and rent reviews smooth.</p></li>
</ul>
""") + sec("""
<h2>Why agencies keep using the same plumber</h2>
<ul class="checks">
<li>Licensed and insured, with QBCC licence and insurance certificates available for your contractor file.</li>
<li>Plumbing and gas from one trade, so a gas heater fault does not mean two callouts.</li>
<li>Honest advice about repair versus replacement, so owners are not paying to patch something that will fail again next month.</li>
<li>Clean, respectful conduct in someone else's home. The work area is left tidy.</li>
<li>Reports written for a property manager to forward, not decode.</li>
</ul>
<p>We service rentals across """ + L("plumber-coomera", "Coomera") + """, """ + L("plumber-pimpama", "Pimpama") + """, """ + L("plumber-beenleigh", "Beenleigh") + """, Ormeau, Helensvale, Hope Island, Loganholme and Shailer Park, and commercial tenancies too; see """ + L("commercial-plumbing", "commercial plumbing") + """. When a tenant rings an agency after hours with water pouring through a ceiling, the shut-off steps on the """ + H("tenant emergency plumbing page") + """ page are the ones to send them while a plumber is arranged. Moyle Plumbing &amp; Gasfitting has been a family business since 1983; the """ + M("Moyle Plumbing website") + """ has the background.</p>
""") + sec("""
<h2>Smoke-free handover: end of tenancy plumbing</h2>
<p>An exit inspection is the best moment to fix small plumbing problems, because the property is empty and the cost can be settled against the bond where misuse is the cause. We check the taps, toilets, hot water unit, drains and any sign of leaks, replace washers and cartridges, clear a slow drain and note anything larger for the owner's approval. The property then goes to the next tenant with a documented condition, which reduces disputes later. For owners who prefer it, the same check can be run annually rather than at each changeover.</p>
"""),
    faqs=[
        ("Can you work to an approval limit?",
         "<p>Yes. Tell us the agency's or owner's limit and we will complete anything under it on the first visit and seek approval before anything above it.</p>"),
        ("Will you deal directly with the tenant?",
         "<p>Yes. We arrange access with the tenant and keep you informed of the outcome, so your time is not spent relaying messages.</p>"),
        ("Do you supply water efficiency certificates?",
         "<p>Yes. After checking the fixtures and fixing any leaks, we issue documentation that records the property meets the water efficiency requirements for passing on consumption charges.</p>"),
        ("Can you tell us if damage was caused by the tenant?",
         "<p>We report what we find: the cause of a blockage, the condition of a fixture, evidence of misuse or ordinary wear. The decision on who pays is yours, but you will have the facts.</p>"),
    ],
    related=[
        ("water-compliancy", "Water compliance"),
        ("hot-water-tempering-valves", "Tempering valves"),
        ("blocked-drains", "Blocked drains"),
        ("hot-water", "Hot water systems"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("plumber-coomera", "Plumber Coomera"),
        ("plumber-pimpama", "Plumber Pimpama"),
        ("plumber-beenleigh", "Plumber Beenleigh"),
    ],
)
