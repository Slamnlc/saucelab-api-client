class Performance:
    def __init__(self, data: dict):
        if data is not None:
            self.job_id: str = data.get('job_id')
            self.job_owner: str = data.get('job_owner')
            self.job_name_hash: str = data.get('job_name_hash')
            self.metric_data: dict = data.get('metric_data')
            self.page_url: str = data.get('page_url')
            self.order_index: int = data.get('order_index')
            self.job_creation_time: str = data.get('job_creation_time')
            self.load_id: str = data.get('load_id')
            self.loader_id: str = data.get('loader_id')
            self.error: str = data.get('error')


class PerformanceJob:
    def __init__(self, data: dict):
        if data is not None:
            self.job_id: str = data.get('job_id')
            self.job_owner: str = data.get('job_owner')
            self.job_name_hash: str = data.get('job_name_hash')
            self.metric_data: PerformanceMetrics = PerformanceMetrics(data.get('metric_data'))
            self.page_url: str = data.get('page_url')
            self.order_index: int = data.get('order_index')
            self.job_creation_time: str = data.get('job_creation_time')
            self.load_id: str = data.get('load_id')
            self.loader_id: str = data.get('loader_id')
            self.error: str = data.get('error')
            self.links = data.get('links')


class PerformanceMetrics:
    def __init__(self, data: dict):
        if data is not None:
            self.rtt: int = data.get('rtt')
            self.load: int = data.get('load')
            self.score: float = data.get('score')
            self.max_rtt: int = data.get('maxRtt')
            self.num_fonts: int = data.get('numFonts')
            self.num_tasks: int = data.get('numTasks')
            self.xhr_size: int = data.get('xhr_size')
            self.font_size: int = data.get('font_size')
            self.xhr_count: int = data.get('xhr_count')
            self.first_paint: int = data.get('firstPaint')
            self.font_count: int = data.get('font_count')
            self.image_size: int = data.get('image_size')
            self.num_scripts: int = data.get('numScripts')
            self.other_size: int = data.get('other_size')
            self.speed_index: int = data.get('speedIndex')
            self.throughput: float = data.get('throughput')
            self.image_count: int = data.get('image_count')
            self.num_requests: int = data.get('numRequests')
            self.other_count: int = data.get('other_count')
            self.script_size: int = data.get('script_size')
            self.first_c_p_u_idle: int = data.get('firstCPUIdle')
            self.requests_size: int = data.get('requestsSize')
            self.script_count: int = data.get('script_count')
            self.document_size: int = data.get('document_size')
            self.requests_count: int = data.get('requestsCount')
            self.total_task_time: int = data.get('totalTaskTime')
            self.document_count: int = data.get('document_count')
            self.num_stylesheets: int = data.get('numStylesheets')
            self.stylesheet_size: int = data.get('stylesheet_size')
            self.time_to_first_byte: int = data.get('timeToFirstByte')
            self.total_byte_weight: int = data.get('totalByteWeight')
            self.dom_content_loaded: int = data.get('domContentLoaded')
            self.first_interactive: int = data.get('firstInteractive')
            self.last_visual_change: int = data.get('lastVisualChange')
            self.max_server_latency: int = data.get('maxServerLatency')
            self.num_tasks_over10ms: int = data.get('numTasksOver10ms')
            self.num_tasks_over25ms: int = data.get('numTasksOver25ms')
            self.num_tasks_over50ms: int = data.get('numTasksOver50ms')
            self.stylesheet_count: int = data.get('stylesheet_count')
            self.first_visual_change: int = data.get('firstVisualChange')
            self.num_tasks_over100ms: int = data.get('numTasksOver100ms')
            self.num_tasks_over500ms: int = data.get('numTasksOver500ms')
            self.total_blocking_time: int = data.get('totalBlockingTime')
            self.server_response_time: int = data.get('serverResponseTime')
            self.first_contentful_paint: int = data.get('firstContentfulPaint')
            self.first_meaningful_paint: int = data.get('firstMeaningfulPaint')
            self.cumulative_layout_shift: int = data.get('cumulativeLayoutShift')
            self.estimated_input_latency: int = data.get('estimatedInputLatency')
            self.largest_contentful_paint: int = data.get('largestContentfulPaint')
            self.main_document_transfer_size: int = data.get('mainDocumentTransferSize')
