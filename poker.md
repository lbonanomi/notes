&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;rss version="2.0"&gt;
&lt;channel&gt;
&lt;title&gt;Help Wanted&lt;/title&gt;
&lt;description&gt;Help Wanted Issues&lt;/description&gt;
&lt;link&gt;https://.github.io/rss/feed.xml&lt;/link&gt;
&lt;item&gt;
        &lt;title&gt;Add Carthage compatibility badge to the README&lt;/title&gt;
        &lt;link&gt;https://github.com/github/Archimedes/issues/38&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[Using [these instructions](https://github.com/Carthage/Carthage/blob/7a0153cc164e301c46527f6e20c886728a0dc218/README.md#declare-your-compatibility).&lt;br/&gt;" ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;Test that license texts match SPDX plain license texts&lt;/title&gt;
        &lt;link&gt;https://github.com/github/choosealicense.com/issues/636&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[We should have a test that each license text in ` ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;Annotating license texts with license rules&lt;/title&gt;
        &lt;link&gt;https://github.com/github/choosealicense.com/issues/441&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[[Comment/question today](https://github.com/github/choosealicense.com/pull/320#issuecomment-230746990) about whether EUPL-1.1 is accurately described reminded me to file this enhancement idea.&lt;br/&gt;&lt;br/&gt;For each license, license rules could be annotated with ranges of text in the license pertinent to the rule. Highlighting of ranges could be turned on/off on individual license pages by selecting in the license rules (permissions/conditions/limitations) table. Very crude mockup taking a very simple case (the one condition of MIT).&lt;br/&gt;&lt;br/&gt;![mit-highlight-condition](https://cloud.githubusercontent.com/assets/40415/16633043/25735510-437c-11e6-84f8-1e504d48f345.png)&lt;br/&gt;&lt;br/&gt;Obviously this is not a big help for MIT, but for longer licenses, it can be tricky to figure out what bits of the license are pertinent for a particular rule, at least if you only want to read once, which is more already than I suspect most people do.&lt;br/&gt;&lt;br/&gt;Such annotations  ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;Add Free Art License&lt;/title&gt;
        &lt;link&gt;https://github.com/github/choosealicense.com/issues/314&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[[Free Art License 1.3](http://artlibre.org/licence/lal/en/)&lt;br/&gt;" ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;I18N&lt;/title&gt;
        &lt;link&gt;https://github.com/github/choosealicense.com/issues/68&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[Would love to see about baking in I18N support to choosealicense.com proper. See #67 and #62&lt;br/&gt;&lt;br/&gt;We already have the bulk of the strings in a single file (` ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;TODO: Configure caching for fast building on travisci&lt;/title&gt;
        &lt;link&gt;https://github.com/github/government.github.com/issues/750&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[Description and details here: https://github.com/gjtorikian/html-proofer#configuring-caching and https://github.com/gjtorikian/html-proofer#caching-with-travis" ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;Alphabetize, other chores should run monthly, open new PRs automatically&lt;/title&gt;
        &lt;link&gt;https://github.com/github/government.github.com/issues/601&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[Currently, the alphabetize script (https://github.com/github/government.github.com/blob/gh-pages/script/alphabetize)  is run manually to clean up the ordering of Organizations in the various data files. (Example: https://github.com/github/government.github.com/pull/58          2). A couple problems with this:&lt;br/&gt;&lt;br/&gt;1. Why do work that a robot 🤖 can do?&lt;br/&gt;2. Since this repo is widely maintained, it's impossible to guarantee that these changes won't create pretty annoying conflicts for other PRs. &lt;br/&gt;&lt;br/&gt;Getting these to a near automated fashio          n would be really cool.&lt;br/&gt;&lt;br/&gt;I'd held off merging a bunch of [open PRs](https://github.com/github/government.github.com/pulls?utf8=%E2%9C%93&q=is%3Apr%20is%3Aopen%20updated%3A%3E2017-07-01) in hopes that I'd get time to work on a solution for this, but alas I have not. So, I figure I'll cro          wd source this to see if anyone has any ideas or fancy the execution.&lt;br/&gt;&lt;br/&gt;## Note&lt;br/&gt;I'd love to use [probot](https://probot.github.io) as the framework for these operations (it's what it was made for), but it's currently a node app and is expecting j/s scripts. Since I try to do as           little with YAML as possible 😉 , this task was never exciting enough to get my attention for very long, and why it floundered. It should be pretty easy as `js-yaml` and basic JS functions should map pretty cleanly.&lt;br/&gt;&lt;br/&gt;By opening this issue, this will be a reminder to me to eventually get           to it too, so no pressure." ]]&gt;&lt;/description&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;XML report for CI&lt;/title&gt;
        &lt;link&gt;https://github.com/github/licensed/issues/52&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[Hi,&lt;br/&gt;&lt;br/&gt;I'm integrating licensed for a poc in our Jenkins pipeline. It could be great to get a report of all licenses checks in an XML formatted file; so we can process it using Jenkins plugins. For now, I have to analyse the `XXX dependencies checked          , XXX warnings found.` string formatted output of `licensed status` command.&lt;br/&gt;&lt;br/&gt;We can consider **licensed results** as **tests results**.&lt;br/&gt;* If all licenses check passed; then the overall test is **passed**.&lt;br/&gt;* If one license is found as unknown, or not matching any of           allowed, ignored or reviewed configs; then the check/test **failed**.&lt;br/&gt;&lt;br/&gt;Standards test output formats such as junit, nunit, mstest, google-test, etc. would be great cos already known by many CI tools. Junit is probably the most used one.&lt;br/&gt;&lt;br/&gt;Organizing tests in \"groups\          " matching the package type (npm, pip, go, etc.) and license type (mit, gpl...) would also allows to \"count\" the type of licenses found... providing some kind of statistics ^&lt;br/&gt;&lt;br/&gt;Example of output in Jenkins test plugin results, processing the XML file could be:&lt;br/&gt;```&lt;br/&gt;P          ackage                  Fail Skip Pass Total&lt;br/&gt;- total                     0    0   69    69&lt;br/&gt;- npm                       0    0   53    53&lt;br/&gt;  - mit                     0    0   45    45&lt;br/&gt;    - package1              0    0    1     1&lt;br/&gt;    - package 2                       ...&lt;br/&gt;    - ...&lt;br/&gt;  - apache-2.0                              3&lt;br/&gt;    - package46&lt;br/&gt;    - ...&lt;br/&gt;  - bsd-3-clause                            1 &lt;br/&gt;    - package49&lt;br/&gt;  - isc                                     1&lt;br/&gt;    - package50&lt;br/&gt;  - un          known                                 3&lt;br/&gt;    - package51             1    0    0     1&lt;br/&gt;    - ...&lt;br/&gt;- go                                       16&lt;br/&gt;  - mit                                    14&lt;br/&gt;    - ...&lt;br/&gt;  - isc                                     1&lt;          br/&gt;    - ...&lt;br/&gt;  - unknown                                 1&lt;br/&gt;    - packagexx             1    0    0     1&lt;br/&gt;    - ...&lt;br/&gt;```&lt;br/&gt;I did not fill the array; but you've got the point ;-)&lt;br/&gt;&lt;br/&gt;Regards,&lt;br/&gt;&lt;br/&gt;Chris" ]]&gt;&lt;/descriptio          n&gt;
&lt;/item&gt;

&lt;item&gt;
        &lt;title&gt;Add a yarn dependency source&lt;/title&gt;
        &lt;link&gt;https://github.com/github/licensed/issues/31&lt;/link&gt;
        &lt;description&gt;&lt;![CDATA[As found in https://github.com/github/licensed/issues/30#issuecomment-386129385&lt;br/&gt;&lt;br/&gt;&gt; The errors appear to be because my package.json file is actually intended for yarn, and uses some syntax that is not npm-compatible&lt;br/&gt;&lt;br/&gt;[Yarn's](          https://yarnpkg.com/) `package.json` files attempt to be compatible with NPM `package.json` files but can contain differences that cause the NPM dependency source to fail.&lt;br/&gt;&lt;br/&gt;It looks like an indicator that yarn should be used and that npm shouldn't be used is the presence of a `yarn.lock          ` file." ]]&gt;&lt;/description&gt;
&lt;/item&gt;
