from _common import *

page = dict(
    slug="plumber-shailer-park", kind="suburb", crumb="Plumber Shailer Park",
    title="Plumber Shailer Park | Large Blocks & Pools | Moyle",
    description="Plumber for Shailer Park's big-block homes: long pipe runs, garden mains, pool top-ups, hot water and drains, from our Yatala base. Call (07) 3807 7327.",
    h1="Plumber Shailer Park",
    eyebrow="Shailer Park QLD 4128",
    intro="<p>A plumber in Shailer Park spends a lot of time outdoors. The suburb's large blocks, established trees and backyard pools mean long pipe runs, garden mains and drains with roots in them, on top of the usual indoor work in homes built through the 1980s and 1990s. Moyle Plumbing &amp; Gasfitting drives up from Yatala and settles the cost before starting.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Shailer Park", area="Shailer Park"),
    body=sec("""
<h2>Big-block plumbing</h2>
<div class="two-col">
<div>
<h3>Outside the house</h3>
<ul>
<li>Long water services from the meter to the house, often in early poly that cracks at fittings.</li>
<li>Garden taps and irrigation connections that leak unnoticed for months.</li>
<li>Pool top-up and backwash connections that have to be plumbed correctly to protect the drinking water supply.</li>
<li>Sewer lines running through gardens planted decades ago, with roots at every joint.</li>
<li>Stormwater from big roofs into pits and drains that silt up.</li>
</ul>
</div>
<div>
<h3>Inside the house</h3>
<ul>
<li>Hot water units serving multiple bathrooms, often undersized for the current household.</li>
<li>Original bathrooms and ensuites due for renovation, with waterproofing that has run its course.</li>
<li>Copper pipework showing pinholes after thirty years.</li>
<li>Kitchen updates needing dishwasher, filter and disposer connections.</li>
<li>Gas cooktops and heaters on original flexible connectors.</li>
</ul>
</div>
</div>
""") + soft("""
<h2>Finding leaks on a large block</h2>
<p>A meter that keeps ticking over on a big block could mean a leak anywhere across hundreds of metres of pipe. We isolate sections one at a time, house from garden, garden from pool, and use acoustic and tracer equipment to locate it before digging. It is the difference between one small hole and a trench across the lawn. Full detail is on the """ + L("leak-repairs", "leak detection page") + """.</p>
<h2>Renovations</h2>
<p>Bathrooms and kitchens across Shailer Park are being redone as the homes reach that age. We take the plumbing side from planning through rough-in to fit-off, and check the hot water capacity before a larger shower or a second ensuite goes in. See """ + L("bathroom-renovations", "bathroom renovation plumbing") + """ and """ + L("bathroom-modifications", "bathroom modifications") + """ for accessibility changes.</p>
""") + sec("""
<h2>Getting here</h2>
<p>Shailer Park is a direct run up the highway from Yatala, next to Loganholme. For urgent faults, shut things off first as the """ + H("Shailer Park emergency plumber page") + """, then ring """ + PHONE + """. We also attend """ + L("plumber-loganholme", "Loganholme") + """, """ + L("plumber-rochedale-south", "Rochedale South") + """ and Cornubia from the same base. Hot water is one of our biggest jobs in the suburb; see the """ + L("hot-water", "hot water page") + """. Moyle Plumbing &amp; Gasfitting, family run since 1983, has more on the """ + M("Moyle Plumbing website") + """.</p>
""") + sec("""
<h2>Gas on the big blocks</h2>
<p>Many Shailer Park homes run gas cooktops, heaters and hot water on LPG, with cylinders beside the house and long pipe runs to the kitchen and the outdoor area. Long runs need correct sizing to keep pressure up when the cooktop and the hot water unit fire together, and older flexible connectors behind appliances are a common leak point. We test the whole installation, replace suspect connectors, and add bayonets for the patio heater or barbecue while we are there. If a natural gas main has since been laid in your street, we can advise whether converting makes sense.</p>
"""),
    faqs=[
        ("Can you find a leak in my garden main without digging up the lawn?",
         "<p>That is the aim. Pressure testing and acoustic detection narrow it to a small area, and the dig is limited to the repair.</p>"),
        ("Is the pool top-up connection a plumber's job?",
         "<p>Yes. A pool auto-fill connected to the drinking water supply needs backflow protection, which is licensed plumbing work.</p>"),
        ("Our hot water runs out with two showers going. What are the options?",
         "<p>A larger storage tank, a continuous flow gas unit, or a heat pump sized for the household. We look at the existing setup and the gas or electrical supply and give you the choices with set prices.</p>"),
        ("Do you clear roots from sewer lines regularly?",
         "<p>Yes. For homes with big trees over the sewer, a routine clean every year or so keeps the line open and avoids emergency callouts.</p>"),
    ],
    related=[
        ("leak-repairs", "Leak detection"),
        ("hot-water", "Hot water"),
        ("bathroom-renovations", "Bathroom renovations"),
        ("blocked-drains", "Blocked drains"),
        ("plumber-loganholme", "Plumber Loganholme"),
        ("plumber-rochedale-south", "Plumber Rochedale South"),
    ],
)
