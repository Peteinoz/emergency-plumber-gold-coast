from _common import *

page = dict(
    slug="frequently-asked-questions", kind="post", crumb="Plumbing FAQs",
    title="Frequently Asked Plumbing Questions | Moyle Plumbing",
    description='Plumbing questions answered by a licensed Gold Coast trade: pricing, water pressure, wipes, hot water life, gas rules and leaks. Call (07) 3807 7327.',
    h1="Frequently asked plumbing questions, answered plainly",
    eyebrow="Handy hints",
    intro="<p>These frequently asked plumbing questions are the ones we hear most often on the phone at Moyle Plumbing &amp; Gasfitting week after week. The answers are short, specific to Queensland and the northern Gold Coast, and written so you can decide what to do next rather than just learn something.</p>",
    breadcrumb=[("handy-hints-blog", "Handy hints")],
    post=dict(published="2026-09-18", modified="2026-09-18"),
    faq_heading="A few more",
    body=sec("""
<h2>Pricing and booking</h2>
<h3>How do you charge?</h3>
<p>The plumber assesses the job and quotes a fixed figure before touching it. You approve it or not. If something unexpected appears mid-job, you hear about it before it is tackled. How the callout itself is charged is explained when you phone.</p>
<h3>Do I need to be home?</h3>
<p>For most jobs someone needs to give access and approve the price. For rentals, the property manager can approve within a limit and the tenant gives access.</p>
<h3>Can you give a quote over the phone?</h3>
<p>For simple, well-described jobs such as a like-for-like hot water swap, often yes. For leaks, drains and anything hidden, an honest price needs a look first.</p>
""") + soft("""
<h2>Water and pressure</h2>
<h3>Why is my water pressure so high?</h3>
<p>Many northern Gold Coast estates are supplied well above the pressure household fixtures are designed for. A pressure limiting valve fitted at the boundary brings it down and stops hoses, mixers and valves failing early.</p>
<h3>Why is my pressure low at one tap?</h3>
<p>Usually a blocked aerator, a partly closed isolation valve or a failing mixer cartridge. If every tap is low, look at the meter tap, the limiting valve or, in older homes, corroded galvanised pipe.</p>
<h3>What is the banging in my pipes?</h3>
<p>Water hammer: a valve closing fast against high pressure. A limiting valve, a hammer arrestor or securing loose pipes fixes it.</p>
<h3>How do I check for a hidden leak?</h3>
<p>Turn everything off, read the meter, wait ten minutes, read it again. Any movement is a leak on your side. Full detail on the """ + L("leak-repairs", "leak detection page") + """.</p>
<h2>Drains and toilets</h2>
<h3>Are flushable wipes really flushable?</h3>
<p>No. They do not break down and they are the most common cause of blocked sewers in the estates. Bin them.</p>
<h3>Why does the toilet gurgle when the shower drains?</h3>
<p>The drain serving both is partly blocked, and air is being pushed back through the toilet trap. Book it before it becomes a full blockage. See """ + L("blocked-drains", "blocked drains") + """.</p>
<h3>Is the gully outside supposed to overflow?</h3>
<p>Yes, when the sewer is blocked. It is there to release outside instead of inside.</p>
""") + sec("""
<h2>Hot water and gas</h2>
<h3>How long should a hot water system last?</h3>
<p>Storage units often pass ten years; continuous flow units can go longer if serviced. Once a tank leaks from its body it is done, whatever its age. The choices are set out on the """ + L("hot-water", "hot water page") + """.</p>
<h3>Why is the bathroom water cooler than the kitchen?</h3>
<p>A tempering valve caps bathroom water at a safe temperature, while the kitchen often branches off upstream of it. That is by design.</p>
<h3>Can I do my own gas work?</h3>
<p>No. In Queensland, fixed gas installations are the preserve of licensed gasfitters. The only thing a householder should do is connect a portable barbecue to its bottle, and isolate the gas if there is a smell.</p>
<h3>Can a plumber work on gas?</h3>
<p>Only with a separate gas licence. Moyle Plumbing &amp; Gasfitting holds both, which is why one tradesperson can do a whole hot water or kitchen job. See """ + L("gas-fitting", "gas fitting") + """.</p>
<h2>Rentals</h2>
<h3>Can my landlord charge me for water?</h3>
<p>Only if the property is individually metered, water efficient with no leaks, and the tenancy agreement says so. See """ + L("water-compliancy", "water compliance") + """.</p>
<h3>Who pays for a blocked drain in a rental?</h3>
<p>Usually the owner, unless the cause was misuse like wipes or fat. Our note on what we found lets the decision rest on facts.</p>
<p>If your question is about something happening right now, head to the """ + H("emergency repairs home page") + """ page for the isolation steps, or read the """ + L("helpful-tips-for-plumbing-emergencies", "emergency tips article") + """. For anything else, ring """ + PHONE + """. The company itself is described on the """ + M("Moyle Plumbing &amp; Gasfitting") + """ main site.</p>
"""),
    faqs=[
        ("Do you work on weekends?",
         "<p>Ring and ask about the day you need. We tell you what is possible rather than making promises on a web page.</p>"),
        ("Do you replace flexible hoses as a preventive job?",
         "<p>Yes, and few jobs in the house return more for the money. Braided hoses under sinks and vanities are the leading cause of flooded homes on the Gold Coast.</p>"),
        ("Can you tell me the age of my hot water unit?",
         "<p>Yes, from the serial number on the compliance plate. Send us a photo of the plate and we can usually work it out.</p>"),
        ("Is it worth a plumbing inspection before buying a house?",
         "<p>For older, canal and acreage homes, definitely. Drain camera footage and a pipe pressure test can shift the price you should pay.</p>"),
    ],
    related=[
        ("helpful-tips-for-plumbing-emergencies", "Emergency tips"),
        ("electrolysis-in-copper-pipe", "Electrolysis in copper pipe"),
        ("hot-water", "Hot water"),
        ("blocked-drains", "Blocked drains"),
        ("water-compliancy", "Water compliance"),
        ("handy-hints-blog", "Handy hints"),
    ],
)
