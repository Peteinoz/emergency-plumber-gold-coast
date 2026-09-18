from _common import *

page = dict(
    slug="contact-us", kind="core", crumb="Contact",
    title="Contact Moyle Plumbing & Gasfitting, Yatala | Call Now",
    description="Contact Moyle Plumbing & Gasfitting at 8 Belair Drive, Yatala QLD 4207. Ring (07) 3807 7327 for plumbing and gas across the northern Gold Coast and Logan.",
    h1="Contact Moyle Plumbing &amp; Gasfitting, Yatala",
    eyebrow="Get in touch",
    intro="<p>The quickest way to contact Moyle Plumbing &amp; Gasfitting is to ring. For anything urgent, a phone call gets a plumber moving from Yatala; for booked work or a quote, email works too. There is no web form on this site: a call or an email reaches a person directly.</p>",
    breadcrumb=[],
    chips=["Phone (07) 3807 7327", "8 Belair Drive, Yatala QLD 4207", "admin@moyleplumbing.com.au", "Family owned since 1983"],
    body=sec("""
<div class="two-col">
<div>
<h2>Phone</h2>
<p><a class="btn btn-navy" href="tel:+61738077327">Call (07) 3807 7327</a></p>
<p>Ring for emergencies, bookings, quotes and property manager work orders. Have your suburb ready and, if something is leaking, tell us what you have already turned off.</p>
<h2>Email</h2>
<p><a class="btn btn-navy" href="mailto:admin@moyleplumbing.com.au">Email admin@moyleplumbing.com.au</a></p>
<p>Best for non-urgent jobs, quotes and work orders. Include your address, a description of the problem and a photo or two if you have them. Property managers can send work orders straight through with tenant contact details.</p>
<h2>Address</h2>
<p>Moyle Plumbing &amp; Gasfitting<br>8 Belair Drive, Yatala QLD 4207</p>
<p>The depot is in the Yatala industrial area between the M1 and Beenleigh. Everyone is normally on the road, so phone before you come by.</p>
</div>
<div>
{map}
</div>
</div>
""") + soft("""
<h2>What to have ready when you ring</h2>
<ol class="steps">
<li>Your suburb and street, so we can tell you a realistic time.</li>
<li>What is happening: water where, gas smell where, which fixtures are affected.</li>
<li>What you have isolated: water meter, gas meter, hot water breaker, fixture valve.</li>
<li>Which kind of heater or gas supply you have, if that is part of the job.</li>
<li>For rentals, whether the property manager has approved the work.</li>
</ol>
<p>If water is running or you can smell gas, isolate first and then ring. Those steps are on the """ + H("Gold Coast urgent plumber page") + """.</p>
""") + sec("""
<h2>Areas and services</h2>
<p>We work across the northern Gold Coast, Beenleigh, Logan, Brisbane's southside and the Redlands acreage; every suburb is listed on the """ + L("suburbs-serviced", "suburbs page") + """. Everything we do is on the """ + L("all-services-available", "services page") + """. Licence and business details are on the """ + L("about-us", "about page") + """, and the company's main website is """ + M("Moyle Plumbing") + """.</p>
"""),
    faqs=[
        ("Do you have a web booking form?",
         "<p>No. Ring or email and you deal with a person directly. That is faster for emergencies and clearer for quotes.</p>"),
        ("Can I text a photo of the problem?",
         "<p>Email a photo to the address above with your details. That way the van arrives stocked for the job.</p>"),
        ("Can I visit the Yatala depot?",
         "<p>Phone ahead. The tradespeople are rarely at the depot during the day, and a call resolves most things faster than a drive.</p>"),
    ],
    related=[
        ("all-services-available", "All services"),
        ("suburbs-serviced", "Suburbs serviced"),
        ("about-us", "About us"),
        ("emergency-plumbing", "Emergency plumbing"),
    ],
)
