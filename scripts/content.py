"""Public copy for the local-only 1.0.0 journal. HTML is developer-authored."""

PRIVACY = {'zh': [('scope',
         '适用范围与开发者',
         '<p>本政策适用于“轻一点”（Lighter，中文完整名称“轻一点：餐食体重活动记录”）1.0.0 记录版、官方网站和技术支持服务。开发与维护方为 Shanghai Qishan Cultural Communication Co., Ltd.，GitHub 账户为 <a '
         'href="{repo_owner}">weizhichao1027-collab</a>，联系邮箱为 <a href="mailto:{email}">{email}</a>。</p><p>App '
         '正在准备发布，尚未提供下载链接。官网展示记录版实际界面与人工示例数据。首发提供餐食、体重、活动、进展与备份，不开放个体计划和动作演示。新功能涉及新的数据处理时，我们会在启用前更新说明。</p><p>App、浏览本网站和主动联系支持是不同的使用场景，下文分别说明。</p>'),
        ('local-data',
         'App 在本机处理哪些信息',
         '<p>你输入的餐食描述、用餐时间、感受、体重数值、单位、测量时间与备注，以及活动类型、日期、时长和主观感受，保存在 App '
         '私有本机存储，用于记录、编辑和查看历史。语言、体重显示单位和时区用于本机展示。</p><p>从旧开发版本恢复的有效备份还可能包含入门草稿、筛查、历史计划、复盘、安全事件与演示进度。这些历史字段仅为数据兼容保留，不会启用个体计划、动作演示或教练提醒。导出和全部删除覆盖这些历史字段。</p><p>App '
         '不调用云端 AI，不向开发者发送健康记录。我们无法远程查看、修改或代你恢复设备中的记录。</p>'),
        ('collection',
         '上传、追踪与第三方 SDK',
         '<p>当前 App 不设账户，不提供后台服务器或云端健康数据库，不上传你的健康记录。没有广告、广告标识符访问、第三方统计分析、会话回放、第三方 AI 调用或跨 App 追踪；没有出售或用于定向广告的数据处理。</p><p>当前未接入 Apple 健康 / '
         'HealthKit、CloudKit、社交登录、支付或订阅 SDK。App 核心记录可离线使用。你主动打开官网、参考资料或外部链接时，浏览器会连接对应的网站，其处理方式见本政策第 7 节。</p>'),
        ('permissions',
         '系统权限与可选功能',
         '<p><strong>文件选择：</strong>导出时由系统文件选择器让你决定保存位置。从备份恢复时，仅读取你选中的 JSON '
         '文件，在本机预览并经你确认后替换记录，不会扫描其他文件。</p><p>记录版不申请通知权限，旧版本安排的教练提醒会被取消。当前不要求访问通讯录、相机、麦克风、照片资料库、定位或 Apple 健康数据。</p>'),
        ('storage',
         '保存期限、安全与恢复',
         '<p>健康记录保存在 App 的私有沙盒目录。健康记录文件启用 iOS '
         '文件保护，并标记为不进入设备备份；保存后进行回读核对，同时保留一份本机上一版本用于异常恢复。必要时可能保留恢复副本或会话状态标记。这些机制属于本机存储，不提供云端同步或远程恢复。</p><p>记录在设备上保留，直到你编辑、删除相关记录、执行全部本机清理，或系统移除 App '
         '及其数据。语言偏好单独保存在系统偏好中，可能在删除健康记录后仍保留。系统的卸载、备份或设备迁移行为受 iOS 管理，不能据此保证健康记录可迁移。</p><p>请使用设备锁屏与系统安全设置，并妥善保管导出文件。任何存储与传输方式都无法保证绝对安全；设备丢失、损坏、卸载 App '
         '或删除数据可能导致记录无法恢复。</p>'),
        ('control',
         '你的查看、修改、导出与删除选择',
         '<p>你可以在 App 中查看和编辑已有记录、删除支持单条删除的记录，并在“设置 → 数据与连接”中选择“导出我的本机记录”或“删除全部本机记录”。导出格式为 '
         'JSON，可能包含筛查、体重、餐食、活动、计划与设置等敏感内容。</p><p>全部删除会清理并核对主记录、上一版本、恢复副本和会话标记。若清理未完成，App 会提示剩余项目并提供重试。请以 App 中的核验结果为准；删除完成后，只有你在 App '
         '外另行保管的有效备份可供主动导入恢复。</p><p><strong>外部副本：</strong>你自行导出到“文件”、iCloud Drive、其他云盘或发送给他人的文件，不会随 App '
         '内的删除自动清除。系统也可能管理导出暂存。请到对应位置分别删除或管理这些副本。你可以在“从备份恢复”中主动选择本 App 导出的有效 JSON '
         '文件，核对日期和记录数量后确认替换当前数据；不会自动合并。恢复不会启用历史个体计划、演示或教练提醒；当前未处理的历史安全事件会保留。</p><p>你可以停止使用并移除 App。开发者未持有你的本机记录，因此无法替你远程访问、删除或恢复它们。</p>'),
        ('website',
         '官网、GitHub 与外部服务',
         '<p>本网站由 GitHub Pages 托管。网站代码不设置 Cookie，不使用 localStorage，不加入访问统计、广告像素、外部字体、第三方视频或聊天嵌入；图片与脚本均随本站提供。FAQ '
         '搜索、界面切换和复制反馈模板在浏览器本地运行，不发送到开发者服务器。</p><p>GitHub 作为托管服务商，会为安全目的记录和保存访客 IP 地址，即使访客没有登录 GitHub；其基础设施还可能处理请求相关信息。该处理由 GitHub 管理，详见 <a '
         'href="https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection" rel="noopener '
         'noreferrer">GitHub Pages 数据收集说明</a>与 <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" '
         'rel="noopener noreferrer">GitHub 隐私声明</a>。我们没有添加独立访问分析。</p><p>你点击邮件链接后，将使用你选择的邮件服务；打开 GitHub 问题页面、Apple 页面或 App '
         '内参考资料链接后，相关服务按各自政策处理请求。外部链接不会自动携带你的 App 健康记录。GitHub Issues 为公开渠道，请勿发布真实健康记录、筛查答案、导出文件或未打码截图。</p><p>支持页搜索词和打开的 FAQ '
         '会显示在页面地址中。不要在搜索栏输入健康资料或个人身份信息；复制页面地址时也请检查其中的查询内容。</p>'),
        ('support-data',
         '主动联系支持时的信息',
         '<p>发送支持邮件或提交问题时，我们会收到你主动提供的邮箱地址 / GitHub 账户、邮件或问题内容、App 与系统版本，以及你选择附上的截图等。用于回复、排查技术问题、处理隐私请求及维护相关处理记录，不用于营销、广告或 AI '
         '训练。</p><p>请使用示例数据描述问题，遮盖个人信息，不要默认发送完整健康记录或 JSON '
         '导出文件。若排查确实需要更多信息，我们会先说明用途与所需最小范围，由你决定是否提供。</p><p>支持通信仅在完成请求、必要后续排查以及适用法律要求所需期间保留；不再需要时删除或去除可识别信息。你可以通过 <a '
         'href="mailto:{email}">{email}</a>请求访问、更正或删除我们持有的支持信息，或撤回基于同意的处理。我们会根据请求与适用规则处理；依法必须保留的信息会说明原因。GitHub 或邮件服务商管理的副本，需按其渠道与规则处理。</p>'),
        ('sharing',
         '共享与跨境处理',
         '<p>当前 App 不把本机健康记录分享给开发者、广告商或第三方，也不自动将健康记录跨境传输。你自主导出文件、选择云盘或向他人发送记录时，相关数据会由你选择的接收方处理。</p><p>网站托管与支持邮件使用 '
         'GitHub、邮件服务等外部基础设施，请求或你主动提交的内容可能在你的所在国家或地区以外处理。处理地点、保存及保障措施以相关服务商政策为准。不要通过公开 GitHub '
         '渠道提交敏感信息。</p><p>我们不会出售支持信息。仅在处理请求所必需的服务提供商范围内，或依法需要履行义务、保护合法权益时处理或披露所持有的信息，并限制在必要范围。</p>'),
        ('adults',
         '成年人使用与健康边界',
         '<p>轻一点是供成年人使用的个人记录工具，不向儿童提供减重计划。记录版不提供诊断、治疗、医疗建议、饮食处方、训练指导或效果保证，不能替代专业医疗人员。</p><p>开发者不主动收集未成年人的健康资料。如果你认为支持通信包含未成年人的个人信息，请联系支持邮箱核实处理。</p>'),
        ('changes',
         '政策更新与联系方式',
         '<p>本政策的更新日期及适用版本显示在页首。数据处理或功能发生变化时，我们会更新此页面；涉及重大变化或需要许可的处理时，会在启用前通过合适方式提示。此前的政策版本可在 <a href="{repo}/commits/main/" rel="noopener '
         'noreferrer">GitHub 更新记录</a>中查看。</p><p>对隐私、数据管理或本政策有疑问，请联系 <a href="mailto:{email}?subject=Lighter%20privacy%20request">{email}</a>，或查看 <a '
         'href="{support}">技术支持页面</a>。请说明请求类型和使用场景，无需提供全部健康记录。</p>')],
 'en': [('scope',
         'Scope and developer',
         '<p>This policy covers Lighter (Chinese name: 轻一点：餐食体重活动记录), version 1.0.0 of the journal, its official website and technical support. The '
         'developer is Shanghai Qishan Cultural Communication Co., Ltd., GitHub account <a href="{repo_owner}">weizhichao1027-collab</a>. Contact <a '
         'href="mailto:{email}">{email}</a>.</p><p>The app is being prepared for release and has no download link yet. Website images show the '
         'actual journal with synthetic example data. This release offers meals, weight, activities, progress and backups. Personalized plans and '
         'exercise demonstrations are not offered. We will explain new data processing before enabling relevant features.</p><p>Using the app, '
         'visiting this website and contacting support are separate situations described below.</p>'),
        ('local-data',
         'Information processed on your device',
         '<p>Meal descriptions, times and feelings; weight values, units, measurement dates and notes; and activity types, dates, durations and '
         'perceived effort stay in private on-device storage for recording, editing and viewing history. Language, display units and time zone '
         'support local presentation.</p><p>A valid backup from an older development version may also contain onboarding drafts, screening answers, '
         'historical plans, reviews, safety events and demonstration progress. These legacy fields are retained for compatibility only. Restoring '
         'them does not enable personalized plans, demonstrations or coaching reminders. Exports and full deletion include these fields.</p><p>The '
         'app does not call cloud AI or send health records to the developer. We cannot remotely view, change or recover records on your '
         'device.</p>'),
        ('collection',
         'Uploads, tracking and third-party SDKs',
         '<p>The current app has no account system, backend server or cloud health database and does not upload your health records. It contains no '
         'ads, advertising identifier access, third-party analytics, session replay, third-party AI calls or cross-app tracking. It does not sell '
         'data or process data for targeted advertising.</p><p>Apple Health / HealthKit, CloudKit, social sign-in, payments and subscription SDKs '
         'are not integrated. Core records and local rules work offline. Opening the website, references or external links connects your browser to '
         'those websites; see section 7.</p>'),
        ('permissions',
         'System permissions and optional features',
         '<p><strong>File selection:</strong> The system file picker lets you choose an export destination. Restoring reads only the JSON file you '
         'select, previews it on your device and replaces records after your confirmation. It does not scan other files.</p><p>The journal does not '
         'request notification permission and cancels coaching reminders scheduled by older versions. It does not request contacts, camera, '
         'microphone, photo library, location or Apple Health permissions.</p>'),
        ('storage',
         'Retention, protection and recovery',
         '<p>Health records are stored in the app’s private sandbox. Record files use iOS file protection and are marked to be excluded from device '
         'backups. Saved data is read back for verification; one previous local version is retained for recovery. A recovery copy or session-state '
         'marker may also be retained when needed. These are local mechanisms and do not provide cloud sync or remote recovery.</p><p>Records remain '
         'on the device until you edit or delete them, clear all local records, or the system removes the app and its data. Language preferences are '
         'stored separately and may remain after health records are deleted. iOS manages offloading, backups and device migration; these do not '
         'guarantee that your health records can be transferred.</p><p>Use device locking and system security settings, and protect exported files. '
         'No storage or transfer method is absolutely secure. Device loss, damage, uninstalling the app or deleting data may make records '
         'unrecoverable.</p>'),
        ('control',
         'Access, edit, export and delete',
         '<p>You can view and edit records, delete individual records where supported, and choose “Export my local records” or “Delete all local '
         'records” under Settings → Data and connections. JSON exports may contain sensitive screening answers, weight, meals, activities, plans and '
         'preferences.</p><p>Deleting all local records clears and verifies the main records, previous version, recovery copy and session marker. If '
         'cleanup is incomplete, the app reports remaining items and offers retry. Rely on the app’s verification result. After deletion, recovery '
         'requires explicitly importing a valid backup you have kept outside the app.</p><p><strong>External copies:</strong> Files you export to '
         'Files, iCloud Drive, other cloud storage or other people are not removed when you delete records inside the app. The system may also '
         'manage temporary export copies. Manage those copies separately at their destinations. Use Restore from backup to choose a valid JSON file '
         'exported by this app. Review its date and record counts, then explicitly confirm replacing current data; records are not merged. Restoring '
         'does not activate historical plans, demonstrations or coaching reminders; current unresolved historical safety reports are '
         'preserved.</p><p>You can stop using and remove the app. The developer does not hold your local records and cannot remotely access, delete '
         'or recover them for you.</p>'),
        ('website',
         'Website, GitHub and external services',
         '<p>This website is hosted on GitHub Pages. Our website code sets no cookies, uses no localStorage, and includes no analytics, ad pixels, '
         'external fonts, embedded third-party videos or chat widgets. Images and scripts are served with the website. FAQ search, screenshot '
         'switching and copying the support template run in your browser without being sent to a developer server.</p><p>GitHub, the hosting '
         'provider, logs and stores visitors’ IP addresses for security, including when visitors are not signed in. Its infrastructure may also '
         'process request information. GitHub manages that processing; see the <a '
         'href="https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection" rel="noopener '
         'noreferrer">GitHub Pages data collection notice</a> and <a '
         'href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener noreferrer">GitHub Privacy '
         'Statement</a>. We have added no separate visitor analytics.</p><p>Email links open your chosen mail service. GitHub issue pages, Apple '
         'pages and the app’s reference links follow their own policies. External links do not automatically include your app health records. GitHub '
         'Issues are public: do not post health records, screening answers, export files or unredacted screenshots.</p><p>Support search terms and '
         'opened FAQs appear in the page URL. Do not enter health details or identifying information into the search field, and check query text '
         'before sharing a link.</p>'),
        ('support-data',
         'Information you send to support',
         '<p>When you email support or submit an issue, we receive the email address or GitHub account, message contents, app and system versions, '
         'and screenshots or other material you choose to send. We use them to reply, troubleshoot, handle privacy requests and keep necessary '
         'resolution records, not for marketing, advertising or AI training.</p><p>Use example data and redact personal information. Do not send '
         'complete health records or JSON exports by default. If troubleshooting needs more information, we will explain the purpose and minimum '
         'scope first so you can decide whether to provide it.</p><p>Support correspondence is retained only as needed to resolve the request, '
         'perform necessary follow-up and meet applicable legal requirements; identifiable information is deleted or removed when no longer needed. '
         'Email <a href="mailto:{email}">{email}</a> to request access, correction or deletion of support information we hold, or withdraw '
         'consent-based processing. We will handle requests under applicable rules and explain legally required retention. Copies managed by GitHub '
         'or mail providers are subject to their own controls.</p>'),
        ('sharing',
         'Sharing and international processing',
         '<p>The current app does not share local health records with the developer, advertisers or third parties and does not automatically '
         'transfer health records internationally. When you choose to export files, select cloud storage or send records to someone, your chosen '
         'recipient processes that information.</p><p>Website hosting and support email use infrastructure such as GitHub and mail services. '
         'Requests or content you submit may be processed outside your country or region. Provider policies describe their locations, retention and '
         'safeguards. Do not use public GitHub channels for sensitive information.</p><p>We do not sell support information. Information we hold is '
         'processed or disclosed only to necessary service providers to handle requests, or as required by law or to protect lawful rights, limited '
         'to what is necessary.</p>'),
        ('adults',
         'Adults and health limitations',
         '<p>Lighter is a personal journal intended for adults. It does not provide weight-loss plans for children. The journal does not provide '
         'diagnosis, treatment, medical advice, dietary prescriptions, exercise instruction or guaranteed outcomes and cannot replace qualified '
         'healthcare professionals.</p><p>The developer does not intentionally collect minors’ health information. If support correspondence '
         'contains a minor’s personal information, contact us so we can review and address it.</p>'),
        ('changes',
         'Updates and contact',
         '<p>The policy date and applicable version appear at the top of this page. We will update the page when features or processing change, and '
         'provide appropriate notice before material changes or processing that requires permission. Previous policy versions are available in the '
         '<a href="{repo}/commits/main/" rel="noopener noreferrer">GitHub history</a>.</p><p>For privacy, data-management or policy questions, email '
         '<a href="mailto:{email}?subject=Lighter%20privacy%20request">{email}</a> or visit <a href="{support}">technical support</a>. Describe the '
         'request and situation; you do not need to provide complete health records.</p>')]}

FAQ = {'zh': [('download', '现在可以下载轻一点吗？', '1.0.0 记录版正在准备发布，尚未提供 App Store 下载链接。真机验收与商店审核完成后，官网会提供经过确认的下载入口。截图使用人工示例资料。'),
        ('offline', '需要注册账号或联网吗？', '无需账号。餐食、体重、活动、历史查看与备份预览均在本机处理；访问官网或发送邮件需要网络。当前没有多设备同步或云端恢复。'),
        ('save',
         '输入后没有出现“已保存”，怎么办？',
         '排队或正在处理不等于已经保存。请留意页面中的保存回执与错误提示，保留当前输入，并按提示重试。设置中的“未完成的保存”会显示尚未可靠写入的项目。排查前不要卸载 App 或删除数据；如果问题持续，请用示例数据说明操作步骤并联系支持。'),
        ('export',
         '怎样导出我的记录？',
         '<ol><li>进入 App“设置 → 数据与连接”。</li><li>选择“导出我的本机记录”，查看并确认导出内容。</li><li>在系统文件选择器中选择保存位置，等待完成提示。</li></ol><p>导出为 '
         'JSON，包含健康相关记录，请妥善保管。选择云盘时，文件会由对应云服务处理。系统取消或未完成，不代表文件已经保存。</p>'),
        ('delete',
         '怎样删除数据？导出的文件会一起删除吗？',
         '在 App“设置 → 数据与连接”中选择“删除全部本机记录”，按提示确认并查看核验结果。若部分清理失败，请使用“重试剩余本机清理”。删除完成后，只有你另行保管的有效 JSON 备份可供主动导入恢复。已导出的文件、邮件附件或其他 App '
         '中的副本不会自动删除，请到原位置单独处理。语言偏好可能仍保留。'),
        ('recovery',
         '换手机、卸载或误删后能恢复吗？',
         '在“设置 → 数据与连接 → 从备份恢复”选择本 App 导出的有效 JSON '
         '文件，核对日期、版本和记录数量，再确认替换当前数据；不自动合并。建议先导出当前记录。旧计划和演示不会激活，旧教练提醒保持关闭。健康记录不进入系统云备份，卸载或换机前请自行导出。没有外部备份时无法保证恢复。'),
        ('reminders', '记录版有提醒或个体计划吗？', '首发不提供教练提醒、个体计划或动作演示。你可以直接记录餐食、体重与已经做过的活动。恢复旧备份不会打开这些功能。'),
        ('weight', '怎样切换语言或体重单位？', '在 App 设置的“日常偏好”中选择语言和体重显示单位。语言可跟随系统或手动选择；当前语言目录包括 13 种语言。改变显示单位不会改写原始测量值。若遇到翻译或格式问题，请提供页面名称、所选语言和示例内容。'),
        ('trend', '进展页展示什么？', '进展页展示已保存的记录数量、最近一次测量和最近 14 条原始体重测量图。全部历史可另行查看与修改。不会给出目标体重、达标日期或健康结论。'),
        ('activity', '怎样记录活动？', '在“今天 → 记活动”或“活动 → 记录自主活动”填写已经做过的活动、日期、时长与感受。可查看、编辑和删除历史。记录版没有训练处方、热量估算或动作演示。'),
        ('health', '轻一点能代替医生或营养师吗？', '不能。它是面向成年人的个人记录工具，不提供诊断、治疗、饮食处方、训练指导或效果保证。健康问题请咨询合格专业人员；紧急情况请联系当地医疗或急救服务。'),
        ('payment', '当前有订阅、支付或 Apple 健康连接吗？', '当前版本没有订阅或支付，也未接入 Apple 健康 / HealthKit、云端 AI、第三方分析或广告。将来若新增相关功能，我们会在启用前更新功能与隐私说明。')],
 'en': [('download',
         'Can I download Lighter now?',
         'Version 1.0.0 of the journal is being prepared for release. There is no App Store link yet. A verified download link will appear after '
         'device acceptance and store review. Screenshots use synthetic example records.'),
        ('offline',
         'Do I need an account or internet connection?',
         'No account is needed. Meals, weight, activities, history and backup previews are processed on your device. Website visits and email need '
         'internet access. There is no multi-device sync or cloud recovery.'),
        ('save',
         'My entry does not show as saved. What should I do?',
         'Queued or processing does not mean saved. Check the receipt and error shown on the page, keep your entry and retry as instructed. Settings '
         'lists incomplete saves that have not been reliably written. Do not uninstall the app or delete data before troubleshooting. If it '
         'persists, describe the steps using example data and contact support.'),
        ('export',
         'How do I export my records?',
         '<ol><li>Open Settings → Data and connections.</li><li>Choose to export your local records and confirm the contents.</li><li>Choose a '
         'destination in the system file picker and wait for confirmation.</li></ol><p>Exports are JSON files containing sensitive health-related '
         'records. Protect them. A cloud destination is managed by that cloud provider. A canceled or unfinished system dialog does not confirm the '
         'file was saved.</p>'),
        ('delete',
         'How do I delete data? Are exports also removed?',
         'Choose to delete all local records under Settings → Data and connections, confirm, and check the verification result. If cleanup partly '
         'fails, retry remaining cleanup. After deletion, restoration requires a valid JSON backup you have kept separately. Exported files, email '
         'attachments and copies in other apps remain until you remove them separately. Language preferences may remain.'),
        ('recovery',
         'Can I recover records after changing phones or uninstalling?',
         'Open Settings → Data and connections → Restore from backup. Select a valid JSON file exported by this app, review the date, version and '
         'record counts, then confirm replacement. Records are not merged. Export current records first. Legacy plans and demonstrations are not '
         'activated, and coaching reminders remain off. Health records are excluded from system cloud backups. Export before uninstalling or '
         'changing devices. Recovery cannot be guaranteed without an external backup.'),
        ('reminders',
         'Does the journal include reminders or personalized plans?',
         'This release does not offer coaching reminders, personalized plans or exercise demonstrations. You can directly record meals, weight and '
         'completed activities. Restoring an older backup does not enable these features.'),
        ('weight',
         'How do I change language or weight units?',
         'Choose language and display units in the app’s everyday preferences. Language can follow the system or be selected manually; the current '
         'catalog contains 13 languages. Changing display units does not rewrite original measurements. For translation or formatting issues, '
         'include the page name, selected language and example text.'),
        ('trend',
         'What does Progress show?',
         'Progress shows saved record counts, the latest measurement and a chart of the 14 most recent original weight measurements. Full history '
         'can be viewed and edited separately. It does not provide target weights, deadlines or health conclusions.'),
        ('activity',
         'How do I record an activity?',
         'Use Today → Log activity or Activity → Record your activity. Enter what you already did, the date, duration and perceived effort. View, '
         'edit and delete history. The journal does not prescribe training, estimate calories or offer exercise demonstrations.'),
        ('health',
         'Can Lighter replace a healthcare professional?',
         'No. It is a personal journal for adults, without diagnosis, treatment, dietary prescriptions, exercise instruction or guaranteed outcomes. '
         'Consult qualified professionals about health concerns and local medical or emergency services for urgent issues.'),
        ('payment',
         'Are there subscriptions, payments or Apple Health connections?',
         'The current version has no subscriptions or payments and does not integrate Apple Health / HealthKit, cloud AI, third-party analytics or '
         'ads. We will update feature and privacy information before enabling relevant new capabilities.')]}
