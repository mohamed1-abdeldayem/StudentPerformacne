import streamlit as st

def render_recommendations_card():
    st.markdown("""
    <!-- Recommendations Section -->
    <h3 class="fw-bold mb-4">Recommendations</h3>
    <div class="row g-3">
      <!-- Recommendation 1 -->
      <div class="col-12 col-md-6">
        <div class="card recommendation-card p-4 h-100">
          <div class="d-flex gap-3">
            <div class="icon-box icon-blue">
              <i class="bi bi-book fs-5"></i>
            </div>
            <div>
              <h5 class="fw-semibold mb-1">Review Key Concepts</h5>
              <p class="text-muted small mb-0">
                Focus on chapters 3 and 7, which showed lower performance in practice tests. Utilize flashcards and summary notes.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Recommendation 2 -->
      <div class="col-12 col-md-6">
        <div class="card recommendation-card p-4 h-100">
          <div class="d-flex gap-3">
            <div class="icon-box icon-yellow">
              <i class="bi bi-clock fs-5"></i>
            </div>
            <div>
              <h5 class="fw-semibold mb-1">Practice Time Management</h5>
              <p class="text-muted small mb-0">
                Work on timed practice questions to improve speed and efficiency under exam conditions. Aim for 2-minute average per question.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Recommendation 3 -->
      <div class="col-12 col-md-6">
        <div class="card recommendation-card p-4 h-100">
          <div class="d-flex gap-3">
            <div class="icon-box icon-green">
              <i class="bi bi-people fs-5"></i>
            </div>
            <div>
              <h5 class="fw-semibold mb-1">Engage in Group Studies</h5>
              <p class="text-muted small mb-0">
                Collaborate with peers to discuss difficult topics and share different perspectives. Explaining concepts to others reinforces your understanding.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Recommendation 4 -->
      <div class="col-12 col-md-6">
        <div class="card recommendation-card p-4 h-100">
          <div class="d-flex gap-3">
            <div class="icon-box icon-red">
              <i class="bi bi-globe fs-5"></i>
            </div>
            <div>
              <h5 class="fw-semibold mb-1">Utilize Online Resources</h5>
              <p class="text-muted small mb-0">
                Explore supplementary materials like video lectures and interactive quizzes available on the course platform. Focus on problem-solving videos.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)