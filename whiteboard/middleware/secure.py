from secure import SecureHeaders, SecurePolicies

csp_value = (
    SecurePolicies.CSP()
    .base_uri(SecurePolicies.CSP().Values.self_)
    .block_all_mixed_content()
    .connect_src(SecurePolicies.CSP().Values.self_, "*.fontawesome.com")
    .frame_src(SecurePolicies.CSP().Values.none)
    .img_src(SecurePolicies.CSP().Values.self_)
)

secure_headers = SecureHeaders(csp=csp_value, feature=True)


def set_secure_headers(get_response):
    def middleware(request):
        response = get_response(request)
        secure_headers.django(response)
        return response

    return middleware
