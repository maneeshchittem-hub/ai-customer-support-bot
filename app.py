import streamlit as st

from agent import chat_with_agent


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Customer Support Bot",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 20%,
            rgba(37, 99, 235, 0.35),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(147, 51, 234, 0.35),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(8, 145, 178, 0.25),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #020617,
            #0f172a,
            #1e1b4b
        );

    background-size: 200% 200%;
    animation: backgroundMove 12s ease infinite;
}


@keyframes backgroundMove {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}


/* Main area */

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}


/* Header */

.chat-header {

    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    padding: 28px;

    border-radius: 24px;

    text-align: center;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.35);

    margin-bottom: 25px;

    border:
        1px solid
        rgba(255,255,255,0.15);
}


.chat-header h1 {

    color: white;

    font-size: 34px;

    margin: 0;
}


.chat-header p {

    color: #e0e7ff;

    font-size: 16px;

    margin-top: 8px;
}


/* Online */

.online {

    display: inline-block;

    margin-top: 10px;

    padding: 6px 15px;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.15);

    color: white;

    font-size: 14px;
}


/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton > button {

    width: 100%;

    text-align: left;

    border: none;

    background: transparent;

    color: #eeeeee;

    border-radius: 10px;

    padding: 10px 12px;

    font-size: 15px;

    height: auto;
}


section[data-testid="stSidebar"]
.stButton > button:hover {

    background:
        rgba(255,255,255,0.10);

    color: white;
}


/* Recent buttons */

.recent-title {

    font-size: 14px;

    color: #9ca3af;

    margin-top: 15px;

    margin-bottom: 5px;
}


/* Chat messages */

[data-testid="stChatMessage"] {

    border-radius: 18px;

    background:
        rgba(255,255,255,0.07);

    border:
        1px solid
        rgba(255,255,255,0.08);

    margin-bottom: 10px;
}


/* Quick buttons */

.quick-button button {

    border-radius: 14px;

    background:
        rgba(255,255,255,0.08);

    color: white;

    border:
        1px solid
        rgba(255,255,255,0.15);

    height: 48px;
}


/* Quick button hover */

.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );

    color: white;
}


/* Hide footer */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


if "recent_questions" not in st.session_state:

    st.session_state.recent_questions = []


if "pending_question" not in st.session_state:

    st.session_state.pending_question = None


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 AI Support")

    st.caption("Your Customer Support Assistant")

    st.divider()


    # -----------------------------
    # SUPPORT OPTIONS
    # -----------------------------

    st.markdown("### 💡 Support")


    if st.button(
        "📦  Order Tracking",
        key="order_tracking",
        use_container_width=True
    ):

        st.session_state.pending_question = (
            "Where is my order ORD1001?"
        )


    if st.button(
        "🚚  Delivery Status",
        key="delivery_status",
        use_container_width=True
    ):

        st.session_state.pending_question = (
            "What is the delivery status of ORD1001?"
        )


    if st.button(
        "🔄  Returns",
        key="returns",
        use_container_width=True
    ):

        st.session_state.pending_question = (
            "What is your return policy?"
        )


    if st.button(
        "💰  Refunds",
        key="refunds",
        use_container_width=True
    ):

        st.session_state.pending_question = (
            "What is your refund policy?"
        )


    if st.button(
        "❌  Cancellation",
        key="cancellation",
        use_container_width=True
    ):

        st.session_state.pending_question = (
            "What is your order cancellation policy?"
        )


    if st.button(
        "📋  Company Policies",
        key="company_policies",
        use_container_width=True
    ):

        st.session_state.pending_question = (
            "What are your main company policies?"
        )


    st.divider()


    # =================================================
    # RECENTS
    # =================================================

    st.markdown("### 🕘 Recents")


    if len(st.session_state.recent_questions) == 0:

        st.caption("No recent questions")


    else:

        for i, question in enumerate(
            st.session_state.recent_questions
        ):

            # Short display text
            display_question = question

            if len(display_question) > 35:

                display_question = (
                    display_question[:35] + "..."
                )


            if st.button(
                display_question,
                key=f"recent_{i}",
                use_container_width=True
            ):

                st.session_state.pending_question = question


    st.divider()


    # =================================================
    # CLEAR CHAT
    # =================================================

    if st.button(
        "🧹  Clear Chat",
        key="clear_chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.recent_questions = []

        st.session_state.pending_question = None

        st.rerun()


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="chat-header">

<h1>🤖 AI Customer Support</h1>

<p>
Your intelligent assistant for orders, shipping and company policies
</p>

<div class="online">
🟢 AI Assistant Online
</div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# CHAT HISTORY
# =====================================================

for role, message in st.session_state.messages:

    with st.chat_message(
        role,
        avatar="👤" if role == "user" else "🤖"
    ):

        st.markdown(message)


# =====================================================
# NORMAL CHAT INPUT
# =====================================================

user_input = st.chat_input(
    "Ask about your order or company policy..."
)


# =====================================================
# GET QUESTION
# =====================================================

question = None


# Sidebar button question
if st.session_state.pending_question:

    question = st.session_state.pending_question

    st.session_state.pending_question = None


# Normal chat input
elif user_input:

    question = user_input


# =====================================================
# PROCESS QUESTION
# =====================================================

if question:

    # ---------------------------------------------
    # Save recent question
    # ---------------------------------------------

    if question in st.session_state.recent_questions:

        st.session_state.recent_questions.remove(
            question
        )


    st.session_state.recent_questions.insert(
        0,
        question
    )


    # Keep only last 10
    st.session_state.recent_questions = (
        st.session_state.recent_questions[:10]
    )


    # ---------------------------------------------
    # Display user
    # ---------------------------------------------

    st.session_state.messages.append(
        ("user", question)
    )


    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(question)


    # ---------------------------------------------
    # AI response
    # ---------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        with st.spinner(
            "🤖 Thinking..."
        ):

            try:

                response = chat_with_agent(
                    question
                )

                st.markdown(response)


                # Save response

                st.session_state.messages.append(
                    (
                        "assistant",
                        response
                    )
                )


            except Exception as e:

                st.error(
                    f"⚠️ Error: {str(e)}"
                )